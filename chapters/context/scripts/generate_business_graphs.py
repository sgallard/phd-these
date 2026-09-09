"""Generates chapters/context/img/plots.pdf from the WAN-IFRA World Press
Trends Outlook 2025-2026 revenue table (resources/context/wan-ifra-report-2026/revenue_report.md).
Run with: pip install matplotlib && python3 generate_business_graphs.py
"""

import matplotlib.pyplot as plt

YEARS = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
YEAR_LABELS = [str(y) for y in YEARS[:-1]] + ["2026\n(forecast)"]

# Values in USD millions, converted to billions for plotting.
PRINT_CIRCULATION = [43300, 42039, 39923, 38048, 36239, 34496, 32833]
PRINT_ADVERTISING = [25401, 23222, 21725, 20400, 19238, 18207, 17294]
DIGITAL_CIRCULATION = [6700, 7347, 8037, 8732, 9423, 10140, 10882]
DIGITAL_ADVERTISING = [10807, 11194, 11564, 11923, 12270, 12602, 12921]
TOTAL_PRINT = [68701, 65261, 61648, 58448, 55477, 52703, 50127]
TOTAL_DIGITAL = [17507, 18541, 19601, 20655, 21693, 22742, 23803]
TOTAL_REVENUE = [86208, 83802, 81249, 79103, 77170, 75445, 73930]

to_b = lambda series: [v / 1000 for v in series]

plt.rcParams.update({"font.size": 13, "axes.titlesize": 13, "legend.fontsize": 11})
fig, (ax_totals, ax_streams) = plt.subplots(1, 2, figsize=(11, 4.6))

# Left panel: total print vs. total digital vs. total industry revenue.
ax_totals.plot(YEARS, to_b(TOTAL_REVENUE), color="black", marker="o", linewidth=2.2, label="Total Industry Revenue")
ax_totals.plot(YEARS, to_b(TOTAL_PRINT), color="#1f77b4", marker="s", linestyle="--", linewidth=2, label="Total Print Revenue")
ax_totals.plot(YEARS, to_b(TOTAL_DIGITAL), color="#2ca02c", marker="^", linestyle=":", linewidth=2, label="Total Digital Revenue")
for series, color in ((TOTAL_REVENUE, "black"), (TOTAL_PRINT, "#1f77b4"), (TOTAL_DIGITAL, "#2ca02c")):
    ax_totals.annotate(f"${series[0]/1000:.1f}B", (YEARS[0], series[0] / 1000), textcoords="offset points", xytext=(-6, 10), color=color, fontweight="bold")
    ax_totals.annotate(f"${series[-1]/1000:.1f}B", (YEARS[-1], series[-1] / 1000), textcoords="offset points", xytext=(-6, 10), color=color, fontweight="bold")
ax_totals.set_xlabel("Year")
ax_totals.set_ylabel("Revenue in Billions (USD)")
ax_totals.set_xticks(YEARS)
ax_totals.set_xticklabels(YEAR_LABELS)
ax_totals.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=1, frameon=False)
ax_totals.grid(True, alpha=0.3)
ax_totals.spines[["top", "right"]].set_visible(False)

# Right panel: the four granular revenue streams.
streams = [
    (PRINT_CIRCULATION, "Print Circulation", "#1f77b4", "o", "-"),
    (PRINT_ADVERTISING, "Print Advertising", "#e377c2", "x", "--"),
    (DIGITAL_ADVERTISING, "Digital Advertising", "#2ca02c", "^", ":"),
    (DIGITAL_CIRCULATION, "Digital Circulation", "#ff7f0e", "d", "-."),
]
for series, label, color, marker, style in streams:
    change_pct = 100 * (series[-1] - series[0]) / series[0]
    ax_streams.plot(YEARS, to_b(series), color=color, marker=marker, linestyle=style, linewidth=2, label=f"{label} ({change_pct:+.0f}%)")
    ax_streams.annotate(f"${series[-1]/1000:.1f}B", (YEARS[-1], series[-1] / 1000), textcoords="offset points", xytext=(-6, 8), color=color, fontweight="bold")
ax_streams.set_xlabel("Year")
ax_streams.set_ylabel("Revenue in Billions (USD)")
ax_streams.set_xticks(YEARS)
ax_streams.set_xticklabels(YEAR_LABELS)
ax_streams.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=1, frameon=False)
ax_streams.grid(True, alpha=0.3)
ax_streams.spines[["top", "right"]].set_visible(False)

fig.tight_layout()
fig.savefig("../img/plots.pdf")
