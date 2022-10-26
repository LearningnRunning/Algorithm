import spacy

nlp = spacy.load("en_core_web_sm")


def anonymize_text(sentences):
    doc = nlp(sentences)
    # 첫 토큰이 이름일 경우 처리
    if doc[0].pos_ == "PROPN":
        sentences = sentences.replace(str(doc[0]), "X" * len(doc[0]), 1)

    for idx in range(1, len(doc)):
        if (doc[idx].pos_ == "PROPN") & (doc[idx - 1].pos_ == "PROPN"):
            # 띄어쓰기로 구별된 고유명사 처리
            sentences = sentences.replace(
                " " + str(doc[idx]), "X" * (len(doc[idx]) + 1), 1
            )
            continue
        else:
            if doc[idx].pos_ == "PROPN":
                # 단일 고유명사 처리
                sentences = sentences.replace(str(doc[idx]), "X" * len(doc[idx]), 1)
    return sentences
