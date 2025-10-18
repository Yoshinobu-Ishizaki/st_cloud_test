import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import font_manager as fm
import os

# 日本語フォントの設定
def setup_japanese_fonts():
    # まずローカルのフォントを試す
    font_candidates = ['Noto Sans JP','Noto Sans CJK JP', 'IPAexGothic', 'MS Gothic', 'Yu Gothic']
    available_fonts = []
    
    for font_name in font_candidates:
        try:
            fp = fm.FontProperties(family=[font_name])
            fn = fm.findfont(fp)
            # 実際にフォントファイルが存在し、デフォルトのフォントでないことを確認
            if os.path.exists(fn) and not fn.endswith('DejaVuSans.ttf'):
                available_fonts.append(font_name)
                st.text(f"フォントが見つかりました: {font_name} ({fn})")
        except Exception as e:
            st.text(f"フォント {font_name} は利用できません: {str(e)}")
    
    if not available_fonts:
        # ローカルフォントが見つからない場合、Noto Sans JPをダウンロード
        try:
            import urllib.request
            import tempfile
            
            # Noto Sans JP フォントをダウンロード
            FONT_URL = "https://raw.githubusercontent.com/googlefonts/noto-cjk/main/Sans/OTF/Japanese/NotoSansJP-Regular.otf"
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.otf') as tf:
                with urllib.request.urlopen(FONT_URL) as response:
                    tf.write(response.read())
                font_path = tf.name
            
            # ダウンロードしたフォントを登録
            fm.fontManager.addfont(font_path)
            available_fonts = ['Noto Sans JP']
            st.text("日本語フォントをダウンロードしました")
        except Exception as e:
            st.warning(f"フォントのダウンロードに失敗しました: {e}")
    
    # フォント設定を適用
    if available_fonts:
        plt.rcParams['font.family'] = available_fonts[0]
    else:
        plt.rcParams['font.family'] = ['sans-serif']

# フォント設定を実行
setup_japanese_fonts()

def main():
    st.title("sin(x) のプロット")
    st.write("x ∈ [0, 2π] における sin(x) の折れ線グラフを表示します。")

    # 現在使用中のフォントファミリーを表示
    current_font = plt.rcParams['font.family']
    st.text(f"使用中のフォント: {', '.join(current_font)}")

    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, color="tab:blue", label="sin(x)")
    ax.set_title("Sin(x)のプロット")  # タイトルを追加
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x)")
    ax.set_xlim(0, 2 * np.pi)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()

    st.pyplot(fig)

if __name__ == "__main__":
    main()
