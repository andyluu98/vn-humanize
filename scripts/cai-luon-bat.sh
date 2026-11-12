#!/usr/bin/env bash
# Cài (hoặc gỡ) khối "luôn bật" của vn-humanize vào CLAUDE.md của người dùng.
# Chạy lại nhiều lần không chèn trùng: khối cũ được thay bằng khối mới.
# Trước mỗi lần ghi, bản cũ của CLAUDE.md được chép vào _backup/ cạnh file.
# Dùng: bash cai-luon-bat.sh [--go] [--file đường-dẫn-CLAUDE.md]
set -euo pipefail

GO=0
CLAUDE_MD="${HOME}/.claude/CLAUDE.md"
while [ $# -gt 0 ]; do
  case "$1" in
    --go) GO=1 ;;
    --file) CLAUDE_MD="$2"; shift ;;
    *) echo "Tham số lạ: $1" >&2; exit 2 ;;
  esac
  shift
done

BAT_DAU='<!-- vn-humanize:bat-dau -->'
KET_THUC='<!-- vn-humanize:ket-thuc -->'
THU_MUC_SKILL="$(cd "$(dirname "$0")/.." && pwd)"
NGUON="${THU_MUC_SKILL}/luon-bat.md"

sao_luu() {
  local thu ten
  thu="$(dirname "$1")/_backup"
  mkdir -p "$thu"
  ten="$(basename "$1" .md)_$(date +%y%m%d-%H%M)"
  local k=2 dich="$thu/$ten.md"
  while [ -e "$dich" ]; do dich="$thu/$ten-$k.md"; k=$((k+1)); done
  ten="$(basename "$dich")"
  cp "$1" "$dich"
  echo "Đã sao lưu bản cũ: $thu/$ten"
}

# In nội dung file, bỏ khối cũ (kể cả dòng đánh dấu).
bo_khoi() {
  awk -v a="$BAT_DAU" -v b="$KET_THUC" '
    index($0, a) { trong=1; next }
    trong && index($0, b) { trong=0; next }
    !trong { print }
  ' "$1"
}

co_khoi=0
if [ -f "$CLAUDE_MD" ] && grep -qF "$BAT_DAU" "$CLAUDE_MD"; then co_khoi=1; fi

tam="$(mktemp)"
trap 'rm -f "$tam"' EXIT

if [ "$GO" -eq 1 ]; then
  if [ "$co_khoi" -eq 0 ]; then echo "Không thấy khối vn-humanize trong $CLAUDE_MD. Không đổi gì."; exit 0; fi
  sao_luu "$CLAUDE_MD"
  bo_khoi "$CLAUDE_MD" | sed -e :a -e '/^\n*$/{$d;N;ba' -e '}' > "$tam"
  cat "$tam" > "$CLAUDE_MD"
  echo "Đã gỡ khối vn-humanize khỏi $CLAUDE_MD"
  exit 0
fi

[ -f "$NGUON" ] || { echo "Không tìm thấy $NGUON" >&2; exit 1; }
khoi="$(awk -v a="$BAT_DAU" -v b="$KET_THUC" '
  index($0, a) { trong=1 }
  trong { sub(/\r$/, ""); print }
  trong && index($0, b) { exit }
' "$NGUON")"
[ -n "$khoi" ] || { echo "luon-bat.md thiếu dòng đánh dấu" >&2; exit 1; }

if [ -f "$CLAUDE_MD" ]; then
  sao_luu "$CLAUDE_MD"
  bo_khoi "$CLAUDE_MD" | sed -e :a -e '/^\n*$/{$d;N;ba' -e '}' > "$tam"
else
  mkdir -p "$(dirname "$CLAUDE_MD")"
  : > "$tam"
fi

{
  if [ -s "$tam" ]; then cat "$tam"; printf '\n'; fi
  printf '%s\n' "$khoi"
} > "${tam}.moi"
mv "${tam}.moi" "$CLAUDE_MD"

if [ "$co_khoi" -eq 1 ]; then echo "Đã cập nhật khối vn-humanize trong $CLAUDE_MD"; else echo "Đã thêm khối vn-humanize vào $CLAUDE_MD"; fi
echo "Mở phiên Claude Code mới để khối có hiệu lực. Gỡ: chạy lại script với --go"
