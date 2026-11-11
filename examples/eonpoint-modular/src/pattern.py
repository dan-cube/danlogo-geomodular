"""EonPoint 方案 A — 辅助图形的生成代码（从提案生成脚本中摘出）。
只学写法：同一个尺寸单位驱动全部构件、按规则排列。颜色用 CSS 变量 var(--f)（主色）与 var(--p)（偏差色）。
不要复用它的造型。"""


def n(x):
    s = f"{x:.2f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def pattern_A(cols=6, rows=8, cell=24, seed=0):
    """点·线·面 rhythm: every row repeats line | plane | point, shifted and turned a quarter each row."""
    shapes = ""
    r0 = cell / 2
    for j in range(rows):
        for i in range(cols):
            kind = (i + j + seed) % 3
            cx, cy = i * cell + r0, j * cell + r0
            rot = ((i // 3 + j) % 4) * 90
            if kind == 0:   # line
                if (i + j) % 2:
                    shapes += f'<rect x="{n(cx - 4.4)}" y="{n(cy - 10)}" width="8.8" height="20" rx="4.4" fill="var(--f)"/>'
                else:
                    shapes += f'<rect x="{n(cx - 10)}" y="{n(cy - 4.4)}" width="20" height="8.8" rx="4.4" fill="var(--f)"/>'
            elif kind == 1:  # plane
                shapes += (f'<path d="M{n(cx)} {n(cy - 10)}A10 10 0 0 1 {n(cx)} {n(cy + 10)}Z" fill="var(--f)" '
                           f'transform="rotate({rot} {n(cx)} {n(cy)}) translate(-3 0)"/>')
            else:            # point
                col = "var(--p)" if (i * 7 + j * 3 + seed) % 5 == 0 else "var(--f)"
                shapes += f'<circle cx="{n(cx)}" cy="{n(cy)}" r="4.6" fill="{col}"/>'
    return shapes, cols * cell, rows * cell
