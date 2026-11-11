# EonPoint 方案 A 的生成代码

- `lettering_engine.py`：标志与中英文字标的参考实现。字用中心线绘制，再统一线宽、端点与转角，所以标志与字共用一套构造。方案 A 用其中的 `S["A"]` 参数与 `mark_A`。
- `pattern.py`：辅助图形（构件阵列）的生成函数 `pattern_A`。
- `palette.json`：定稿色板（生成 · 墨 · 弁柄），可用 `scripts/` 或 danlogo-maker 的工具检查对比度。

注意：`lettering_engine.py` 里方案 A 的颜色是早期版本（后来被否的蓝色），定稿颜色以 `palette.json` 和 `cases/eonpoint-modular/case.md` 为准。字形只适用于 EonPoint / 亿触点。**学写法，不复用造型和字形。**

本目录不在 MIT 许可范围内：设计版权归 dan-cube 所有，保留一切权利（见仓库根目录的 `LICENSE`）。
