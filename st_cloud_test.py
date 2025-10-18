import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import font_manager as fm
import os

# 日本語フォントの設定（システムにインストールされているすべてのフォントを探す）
font_files = fm.findSystemFonts()  # デフォルトの検索パスを使用

# 使用可能な日本語フォントを確認
available_fonts = []
has_noto_cjk = False

# Noto CJK フォントの存在確認
for font_file in font_files:
    if 'NotoSansCJK' in font_file:
        has_noto_cjk = True
        break

# フォントの確認と登録
for font_name in ['IPAexGothic', 'MS Gothic', 'Yu Gothic']:
    try:
        fm.findfont(font_name, fallback=False)
        available_fonts.append(font_name)
    except:
        continue

# Noto Sans CJK JP が見つかった場合は追加
if has_noto_cjk:
    available_fonts.insert(0, 'Noto Sans CJK JP')  # 優先度を最も高く設定

if available_fonts:
    # 使用可能なフォントが見つかった場合はそれを設定
    font_name = available_fonts[0]  # 最初に見つかったフォントを使用
    plt.rcParams['font.family'] = 'sans-serif'  # デフォルトファミリーを設定
    plt.rcParams['font.sans-serif'] = [font_name] + plt.rcParams['font.sans-serif']  # 日本語フォントを先頭に追加
else:
    # 使用可能なフォントが見つからない場合はデフォルトのフォントを使用
    plt.rcParams['font.family'] = 'sans-serif'

def main():
    st.title("sin(x) のプロット")
    st.write("x ∈ [0, 2π] における sin(x) の折れ線グラフを表示します。")

    # 現在使用中のフォントファミリーを表示
    current_font = plt.rcParams['font.family']
    if isinstance(current_font, list):
        st.text(f"使用中のフォント: {', '.join(current_font)}")
    else:
        st.text(f"使用中のフォント: {current_font}")

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
