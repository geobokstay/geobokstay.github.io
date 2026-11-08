# 거복스테이 홈페이지

Cloudflare Workers(정적 파일)로 배포합니다. `wrangler.jsonc`가 `docs/` 폴더를 그대로 올립니다.

- `docs/index.html` — 홈페이지 한 장
- `docs/img/` — 사진 (webp, `_s`는 갤러리 작은 사진)
- `docs/fonts/` — 넥슨 Lv1 고딕
- 실시간 예약현황은 예약장부 캘린더를 읽는 Apps Script 주소를 씁니다.

## 문구를 바꾼 뒤
`python3 tools/subset_fonts.py` 를 실행해 글꼴을 다시 만드세요. (원본 글꼴: `tools/fonts-full/`)
