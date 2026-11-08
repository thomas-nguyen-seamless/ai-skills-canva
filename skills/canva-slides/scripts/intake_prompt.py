#!/usr/bin/env python3
"""Print a tailored design-intake questionnaire BEFORE building a deck.

Usage:
  python3 intake_prompt.py --topic "quy luật phủ định của phủ định" [--source textbook|pdf|none]
                           [--minutes 15] [--slides 20] [--lang vi|en]

Why: half the rework in deck projects comes from guessing the look. The questions below are
generated from the topic (a law needs a cycle/chain decision, a history deck needs a timeline,
a data claim needs real numbers) and always cover theme, density, visual language, imagery,
citation fidelity, examples and special slides. Ask 4-6 at a time, offer the default, never ask
something the source or the brief already answers.
"""
import argparse
import re

VI = {
    "head": "BỘ CÂU HỎI TRƯỚC KHI DỰNG SLIDE",
    "must": "1. BẮT BUỘC (nếu thiếu thì không dựng được)",
    "style": "2. ĐỊNH DẠNG VÀ PHONG CÁCH (hỏi trước, đừng đoán)",
    "topic": "3. CÂU HỎI RIÊNG CHO CHỦ ĐỀ NÀY",
    "how": "4. CÁCH HỎI",
}

EN = {
    "head": "DESIGN INTAKE - ASK BEFORE BUILDING",
    "must": "1. MUST KNOW (cannot build without)",
    "style": "2. FORMAT AND LOOK (ask, do not guess)",
    "topic": "3. QUESTIONS SPECIFIC TO THIS TOPIC",
    "how": "4. HOW TO ASK",
}

MUST_VI = [
    "Mục đích: trình bày trên lớp, bảo vệ đồ án, báo cáo nội bộ, hay tài liệu tự đọc?",
    "Khán giả: sinh viên năm mấy, giảng viên chấm, hay đồng nghiệp? Họ đã biết gì trước?",
    "Thời lượng nói (phút) và số slide mong muốn (khoảng)?",
    "Nguồn bắt buộc: giáo trình/PDF nào, có phải bám đúng câu chữ không?",
    "Deliverable: chỉ slide, hay kèm ghi chú người nói, Q&A, bản in?",
    "Ngôn ngữ và văn phong: tiếng Việt học thuật, thuyết trình, hay thân mật?",
]

STYLE_VI = [
    ("Nền và màu", "sáng (#F7F8FA) hay tối (navy)? Có màu nhận diện của trường/khoa không? Gửi mã màu/logo nếu có.", "sáng + 1 màu nhấn xanh"),
    ("Mật độ", "ít chữ (presenter, <= 25 từ/slide), vừa (talk, <= 40), hay chi tiết (document, <= 75)?", "talk"),
    ("Ngôn ngữ thị giác", "tranh khắc/minh hoạ vẽ, vector phẳng, ảnh thật, chỉ sơ đồ, hay tối giản không hình?", "sơ đồ native + 1 tranh khắc"),
    ("Kiểu chữ", "sans hiện đại (Arial/Inter) hay serif học thuật? Cỡ chữ cho phòng học lớn hay đọc trên máy?", "sans, body 34-38 px"),
    ("Bố cục", "lưới thẻ đều, cột đôi, timeline ngang, hay full-bleed ảnh? Có cần slide mục lục?", "lưới thẻ + mục lục"),
    ("Hình ảnh", "dùng ảnh của bạn, ảnh AI vẽ, ảnh public domain, hay không dùng ảnh? Có ảnh nào bắt buộc xuất hiện?", "chỉ ảnh người dùng/AI cho trang bìa + minh hoạ"),
    ("Ví dụ", "bao nhiêu ví dụ, ở những lĩnh vực nào (tự nhiên, xã hội, tư duy, máy tính)? Có ví dụ nào bắt buộc?", "3-4 ví dụ khác lĩnh vực"),
    ("Trích dẫn", "giữ nguyên câu chữ nguồn hay được diễn giải? Có cần ghi số trang không?", "giữ nguyên + ghi số trang"),
    ("Slide đặc biệt", "có mục lục, câu hỏi ôn tập, phần cảm ơn, tên người trình bày + ngày không?", "mục lục + tổng kết + cảm ơn"),
    ("Ràng buộc", "số slide tối thiểu/tối đa, 16:9, cần in A4, hay cần bản PDF gửi trước?", "16:9, PDF kèm"),
    ("Điều cấm", "có gì tuyệt đối không được sai (thuật ngữ, số liệu, thứ tự lý luận)?", "thuật ngữ giáo trình"),
]

MUST_EN = [
    "Purpose: class talk, defence, internal report, or self-reading document?",
    "Audience: which year, lecturer grading, or colleagues? What do they already know?",
    "Speaking time (minutes) and target slide count?",
    "Required source: which textbook/PDF, and must the wording be verbatim?",
    "Deliverable: slides only, or notes, Q&A sheet, print version?",
    "Language and register: academic Vietnamese, presentation, or casual?",
]

STYLE_EN = [
    ("Ground and colour", "light (#F7F8FA) or dark (navy)? Brand colours from school/faculty? Send hex or logo.", "light + one blue accent"),
    ("Density", "sparse (presenter, <= 25 words), medium (talk, <= 40), or detailed (document, <= 75)?", "talk"),
    ("Visual language", "engraving/illustration, flat vector, photography, diagrams only, or minimal?", "native diagrams + one engraving"),
    ("Type", "modern sans (Arial/Inter) or academic serif? Lecture-hall size or screen reading?", "sans, body 34-38 px"),
    ("Layout", "equal card grid, two columns, horizontal timeline, full-bleed image? Agenda slide?", "card grid + agenda"),
    ("Imagery", "your own photos, AI art, public domain, or none? Any image that must appear?", "user/AI art for cover and illustration"),
    ("Examples", "how many, from which domains (nature, society, thought, computing)? Any mandatory case?", "3-4 across domains"),
    ("Citations", "verbatim source wording or paraphrase? Page numbers required?", "verbatim + page numbers"),
    ("Special slides", "agenda, review questions, thanks, presenter name and date?", "agenda + summary + thanks"),
    ("Constraints", "min/max slides, 16:9, printable A4, PDF to send ahead?", "16:9 + PDF"),
    ("Hard bans", "what must never be wrong (terms, numbers, order of reasoning)?", "course terminology"),
]

RULES = [
    (r"quy luật|định luật|law|nguyên lý|principle", [
        "Minh hoạ cơ chế bằng chuỗi thẳng, vòng tuần hoàn, hay đường xoáy ốc? (mỗi kiểu truyền một ý khác nhau)",
        "Có cần sơ đồ cho từng bước, hay chỉ một sơ đồ tổng?",
        "Có cần so sánh quy luật này với các quy luật còn lại trong chương?",
    ], [
        "Illustrate the mechanism as a straight chain, a cycle, or a spiral? (each says something different)",
        "A diagram per step, or one overview diagram?",
        "Compare this law with the other laws in the chapter?",
    ]),
    (r"triết|mác|lênin|philosoph|khái niệm|phạm trù|concept", [
        "Bám đúng câu chữ giáo trình, hay được phép diễn giải cho dễ hiểu?",
        "Giữ đúng số đặc trưng/tính chất như giáo trình nêu, hay bổ sung từ nguồn khác (và ghi rõ)?",
        "Ví dụ minh hoạ nên nằm trong giáo trình, ngoài giáo trình, hay cả hai?",
    ], [
        "Verbatim textbook wording, or may it be paraphrased for clarity?",
        "Keep exactly the features the textbook lists, or add from other sources (and label them)?",
        "Examples from inside the textbook, outside it, or both?",
    ]),
    (r"lịch sử|history|giai đoạn|thời kỳ|period|triều|war", [
        "Dùng timeline ngang theo năm, hay chia theo giai đoạn?",
        "Có mốc thời gian nào bắt buộc và tuyệt đối không được sai?",
        "Có cần bản đồ/bối cảnh địa lý không?",
    ], [
        "Horizontal year timeline, or grouped by period?",
        "Any dates that are mandatory and must never be wrong?",
        "A map or geographic context?",
    ]),
    (r"so sánh|compare|versus|khác nhau|difference|ưu nhược", [
        "Bảng so sánh mấy cột, và tiêu chí so sánh là gì?",
        "Kết luận nên nằm ở hàng cuối bảng hay một slide riêng?",
    ], [
        "Comparison table with how many columns, and which criteria?",
        "Should the conclusion be the last table row or its own slide?",
    ]),
    (r"quy trình|process|các bước|step|pipeline|workflow", [
        "Đánh số các bước, hay dùng mũi tên không số (nếu không phải chuỗi bắt buộc)?",
        "Có nhánh rẽ/điều kiện nào cần vẽ không?",
    ], [
        "Number the steps, or use unnumbered arrows (if the order is not strict)?",
        "Any branches or conditions to draw?",
    ]),
    (r"số liệu|data|thống kê|statistic|%|doanh thu|metric", [
        "Số liệu lấy từ đâu, có được phép làm tròn?",
        "Dùng bảng, cột, hay một con số lớn duy nhất mỗi slide?",
        "Số nào là số thật, số nào chỉ minh hoạ?",
    ], [
        "Where do the numbers come from, and may they be rounded?",
        "Table, bars, or one big number per slide?",
        "Which numbers are real and which are illustrative?",
    ]),
    (r"sinh|vòng đời|tế bào|biology|cycle|chu kỳ", [
        "Vẽ vòng đời khép kín hay chuỗi có điểm dừng?",
        "Có cần ảnh thật của từng giai đoạn hay chỉ sơ đồ?",
    ], [
        "Closed life-cycle loop or an open chain?",
        "Real photos per stage, or diagrams only?",
    ]),
    (r"kiến trúc|hệ thống|architecture|network|hạ tầng", [
        "Sơ đồ khối theo tầng hay theo luồng dữ liệu?",
        "Có cần chú thích công nghệ cụ thể (tên sản phẩm/phiên bản) không?",
    ], [
        "Layered block diagram or data-flow diagram?",
        "Annotate specific technologies (product names/versions)?",
    ]),
]

DEFAULT_VI = [
    "Slide này để định nghĩa, nêu tính chất, hay cho ví dụ? Có cần bảng so sánh không?",
    "Có phần nào bắt buộc phải xuất hiện đúng thứ tự không?",
]
DEFAULT_EN = [
    "Is this slide for a definition, its properties, or a worked example? Any comparison table?",
    "Is any part required to appear in an exact order?",
]

HOW_VI = [
    "Hỏi 4-6 câu một lượt, kèm mặc định để người dùng chỉ cần chọn hoặc nói 'mặc định'.",
    "Câu hỏi phải suy ra từ nội dung người dùng đã nêu, không hỏi chung chung.",
    "Không hỏi lại thứ đã có trong nguồn, trong brief, hay trong deck cũ.",
    "Chốt xong thì ghi câu trả lời vào plan.json mục 'design' trước khi dựng.",
]
HOW_EN = [
    "Ask 4-6 at a time, each with a default so the user can just pick or say 'default'.",
    "Derive questions from the content the user already gave, never generic filler.",
    "Never re-ask something the source, brief or existing deck already answers.",
    "Write the answers into plan.json under 'design' before building.",
]


def pick(topic):
    t = topic.lower()
    for pat, vi, en in RULES:
        if re.search(pat, t):
            return vi, en
    return DEFAULT_VI, DEFAULT_EN


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--source", default="none", choices=["textbook", "pdf", "none"])
    ap.add_argument("--minutes", type=int, default=None)
    ap.add_argument("--slides", type=int, default=None)
    ap.add_argument("--lang", default="vi", choices=["vi", "en"])
    a = ap.parse_args()
    L = VI if a.lang == "vi" else EN
    must = MUST_VI if a.lang == "vi" else MUST_EN
    style = STYLE_VI if a.lang == "vi" else STYLE_EN
    how = HOW_VI if a.lang == "vi" else HOW_EN
    tvi, ten = pick(a.topic)
    topic_q = tvi if a.lang == "vi" else ten

    W = []
    W.append(f"{L['head']}: {a.topic}")
    if a.minutes or a.slides:
        W.append(f"({a.minutes or '?'} min, {a.slides or '?'} slides, source: {a.source})")
    W.append("")
    W.append(L["must"])
    for q in must:
        W.append(f"- {q}")
    W.append("")
    W.append(L["style"])
    for label, q, default in style:
        W.append(f"- {label}: {q} [" + ("mặc định" if a.lang == "vi" else "default") + f": {default}]")
    W.append("")
    W.append(L["topic"])
    for q in topic_q:
        W.append(f"- {q}")
    W.append("")
    W.append(L["how"])
    for h in how:
        W.append(f"- {h}")
    print("\n".join(W))


if __name__ == "__main__":
    main()
