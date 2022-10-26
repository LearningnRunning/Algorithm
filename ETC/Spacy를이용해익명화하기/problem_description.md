# 문제설명
사람의 이름을 포함한 문장에서 이름만 익명으로 바꾸는 함수를 작성하십시오.
예시 문장은 영어로 제시되며, 이름 알파벳 개수 만큼 'X' 문자로 바꾸는 anonymize_text 함수를 작성하십시오.
단, 성과 이름 사이에 공백문자가 있다면 그 역시 'X'로 변환해야합니다.


anonymize_text('John is old') == 'XXXX is old'
anonymize_text('Mark Oldham ate an apple') == 'XXXXXXXXXXX ate an apple'

## 사용 가능한 패키지/라이브러리
Spacy en_web_core_sm 모델

## 작동 예시
anonymize_text 함수는 다음 예제와 같이 작동해야 합니다.

anonymize_text('John is old') == 'XXXX is old'
anonymize_text('Mark Oldham이 사과를 먹었습니다') == 'XXXXXXXXXXX가 사과를 먹었습니다'

### 힌트
귀하의 솔루션은 정확성을 기준으로 평가됩니다. 성능 및 코딩 스타일은 평가되지 않습니다.


## Spacy POS Tags List
|POS|DESCRIPTION|EXAMPLES|
|---|-----------|---------|
ADJ|	adjective|	*big, old, green, incomprehensible, first*|
ADP|	adposition|	*in, to, during*|
ADV|	adverb|	*very, tomorrow, down, where, there*|
AUX|	auxiliary|	*is, has (done), will (do), should (do)*|
CONJ|	conjunction|	*and, or, but*|
CCONJ|	coordinating conjunction|	*and, or, but*|
DET|	determiner|	*a, an, the*|
INTJ|	interjection|	*psst, ouch, bravo, hello*|
NOUN|	noun|	*girl, cat, tree, air, beauty*|
NUM|	numeral|	*1, 2017, one, seventy-seven, IV, MMXIV*|
PART|	particle|	*’s, not,*|
PRON|	pronoun|	*I, you, he, she, myself, themselves, somebody*|
PROPN|	proper| noun	*Mary, John, London, NATO, HBO*|
PUNCT|	punctuation|	*., (, ), ?*|
SCONJ|	subordinating conjunction|	*if, while, that*|
SYM|	symbol|	*$, %, §, ©, +, −, ×, ÷, =, :), 😝*|
VERB|	verb|	*run, runs, running, eat, ate, eating*|
X|	other|	*sfpksdpsxmsa*|
SPACE|	space|