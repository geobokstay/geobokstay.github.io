# 거복스테이 홈페이지

Cloudflare Workers(정적 파일)로 배포합니다. `wrangler.jsonc`가 `public/` 폴더를 그대로 올립니다.

- `public/index.html` — 홈페이지 한 장
- `public/img/` — 사진 (webp, `_s`는 갤러리 작은 사진)
- `public/fonts/` — 넥슨 Lv1 고딕
- 실시간 예약현황은 예약장부 캘린더를 읽는 Apps Script 주소를 씁니다.
