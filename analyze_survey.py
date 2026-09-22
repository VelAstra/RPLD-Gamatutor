import zipfile
import xml.etree.ElementTree as ET
import re
from collections import Counter
import statistics

def col2num(col):
    num = 0
    for c in col:
        num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num - 1

path = r'c:\Users\Rayhan\Documents\Antigravity\KS RPLD\Survei Validasi Kebutuhan Pengguna terhadap Solusi Tutorial Animatif.xlsx'
with zipfile.ZipFile(path, 'r') as z:
    shared_strings_xml = z.read('xl/sharedStrings.xml')
    sheet_xml = z.read('xl/worksheets/sheet1.xml')

ss_root = ET.fromstring(shared_strings_xml)
shared_strings = []
for si in ss_root.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
    t = si.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
    if t is not None and t.text:
        shared_strings.append(t.text)
    else:
        text_parts = [elem.text for elem in si.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t') if elem.text]
        shared_strings.append(''.join(text_parts))

sheet_root = ET.fromstring(sheet_xml)
matrix = {}
max_col = 0
max_row = 0

for row_el in sheet_root.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
    r_idx = int(row_el.get('r')) - 1
    if r_idx > max_row: max_row = r_idx
    for c in row_el.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
        ref = c.get('r')
        col_letter = re.match(r'([A-Z]+)', ref).group(1)
        c_idx = col2num(col_letter)
        if c_idx > max_col: max_col = c_idx
        
        t = c.get('t')
        v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
        val = ''
        if v is not None and v.text is not None:
            if t == 's':
                val = shared_strings[int(v.text)]
            else:
                val = v.text
        matrix[(r_idx, c_idx)] = val

grid = []
for r in range(max_row + 1):
    row_vals = [matrix.get((r, c), '') for c in range(max_col + 1)]
    grid.append(row_vals)

header = grid[0]
data = grid[1:]
n = len(data)

print(f"Total respondents: {n}")
print(f"Total columns: {len(header)}")

output_report = []
output_report.append(f"# LAPORAN ANALISIS DATA SURVEI EMPIRIS (N = {n})\n")

for c_idx in range(len(header)):
    col_name = header[c_idx]
    values = [r[c_idx] for r in data]
    
    report_block = [f"### [Kolom {c_idx+1}] {col_name}"]
    
    # Check if empty
    non_empty = [v for v in values if v.strip()]
    if not non_empty:
        report_block.append("*(Semua jawaban kosong)*\n")
        output_report.append("\n".join(report_block))
        continue
        
    # Check numeric
    numeric_vals = []
    is_numeric = True
    for v in non_empty:
        try:
            numeric_vals.append(float(v))
        except:
            is_numeric = False
            break
            
    if is_numeric and len(numeric_vals) == len(non_empty):
        avg = statistics.mean(numeric_vals)
        median = statistics.median(numeric_vals)
        std = statistics.stdev(numeric_vals) if len(numeric_vals) > 1 else 0.0
        counts = Counter(numeric_vals)
        report_block.append(f"- **Tipe Data**: Numerik / Skala Likert (N={len(numeric_vals)})")
        report_block.append(f"- **Rata-rata (Mean)**: {avg:.2f} / 5.00")
        report_block.append(f"- **Median**: {median:.2f}")
        report_block.append(f"- **Standar Deviasi**: {std:.2f}")
        report_block.append("- **Distribusi Frekuensi**:")
        for k in sorted(counts.keys()):
            pct = (counts[k] / n) * 100
            report_block.append(f"  - Skala {int(k) if k.is_integer() else k}: {counts[k]} responden ({pct:.1f}%)")
    else:
        # Check if comma-separated multi-select
        has_comma = any(',' in v for v in values if v)
        report_block.append(f"- **Tipe Data**: {'Pilihan Ganda (Multi-select)' if has_comma else 'Teks / Pilihan Tunggal'}")
        
        if has_comma:
            # Multi-select
            all_parts = []
            for v in values:
                if v.strip():
                    parts = [p.strip() for p in re.split(r',\s*', v) if p.strip()]
                    all_parts.extend(parts)
            counts = Counter(all_parts)
            report_block.append("- **Frekuensi Pilihan (Persentase terhadap total responden)**:")
            for item, count in counts.most_common():
                pct = (count / n) * 100
                report_block.append(f"  - {item}: {count}/{n} ({pct:.1f}%)")
        else:
            # Single select or qualitative text
            counts = Counter([v.strip() for v in values if v.strip()])
            report_block.append("- **Frekuensi Jawaban**:")
            for item, count in counts.most_common():
                pct = (count / n) * 100
                report_block.append(f"  - \"{item}\": {count}/{n} ({pct:.1f}%)")
                
    report_block.append("")
    output_report.append("\n".join(report_block))

full_report_text = "\n".join(output_report)
with open(r"c:\Users\Rayhan\Documents\Antigravity\KS RPLD\survey_analysis_report.md", "w", encoding="utf-8") as f:
    f.write(full_report_text)

print("Analysis report written successfully to survey_analysis_report.md")
