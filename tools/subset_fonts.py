# 글꼴을 홈페이지에 실제로 쓰인 글자만 남겨 작게 만듭니다 (문구를 바꾼 뒤 다시 실행).
# 실행: python3 tools/subset_fonts.py   (pip install fonttools brotli 필요)
import re, subprocess, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / 'public/index.html').read_text(encoding='utf-8')
text = re.sub(r'<[^>]+>', '', html)
extra = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz·…‹›×≡▲()~%/,:.-!?‘’“”&+ '
hangul_common = '가나다라마바사아자차카타파하'  # 여유분
chars = ''.join(sorted(set(text + extra + hangul_common)))
(root / 'tools/chars.txt').write_text(chars, encoding='utf-8')
(root / 'public/fonts').mkdir(exist_ok=True)
for w in ['Light', 'Regular', 'Bold']:
    subprocess.run(['pyftsubset', str(root / f'tools/fonts-full/NEXONLv1Gothic{w}.woff2'),
                    f'--text-file={root / "tools/chars.txt"}', '--flavor=woff2',
                    f'--output-file={root / f"public/fonts/NEXONLv1Gothic{w}.woff2"}'], check=True)
print(len(chars), 'chars')
