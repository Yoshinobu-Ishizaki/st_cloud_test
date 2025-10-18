import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import font_manager as fm
import os

# see https://discuss.streamlit.io/t/font-for-japanese-character-in-matplotlib-and-seaborn/37206/9
fpath = os.path.join(os.getcwd(), "streamlit_app/Noto_Sans_JP/NotoSansJP-Regular.otf")
prop = fm.FontProperties(fname=fpath)
font_dir = ['streamlit_app/Noto_Sans_JP']
for font in fm.findSystemFonts(font_dir):
    fm.fontManager.addfont(font)

plt.rcParams['font.family'] = ['Noto Sans JP','IPAexGothic', 'MS Gothic', 'Yu Gothic','sans-serif']

def main():
    st.title("sin(x) のプロット")
    st.write("x ∈ [0, 2π] における sin(x) の折れ線グラフを表示します。")

    # 現在使用中のフォントファミリーを表示
    current_font = plt.rcParams['font.family']
    st.text(f"使用中のフォント候補: {', '.join(current_font)}")

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
