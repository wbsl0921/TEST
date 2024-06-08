import pandas as pd
from Levenshtein import distance as levenshtein_distance

# 챗봇 클래스를 정의하는 클래스
class SimpleChatBot:
    # 챗봇 객체를 초기화하는 메서드
    def __init__(self, filepath):
        # CSV 파일로부터 질문과 답변 데이터를 불러와서 self.questions와 self.answers에 저장
        self.questions, self.answers = self.load_data(filepath)

    # CSV 파일로부터 질문과 답변 데이터를 불러오는 메서드
    def load_data(self, filepath):
        # 주어진 파일 경로에서 CSV 파일을 읽어옴
        data = pd.read_csv(filepath)
        # 'Q' 열의 데이터를 리스트로 변환하여 questions에 저장
        questions = data['Q'].tolist()
        # 'A' 열의 데이터를 리스트로 변환하여 answers에 저장
        answers = data['A'].tolist()
        # questions와 answers 리스트를 반환
        return questions, answers

    # 입력 문장에 가장 잘 맞는 답변을 찾는 메서드
    def find_best_answer(self, input_sentence):
        # 각 질문과 입력 문장의 레벤슈타인 거리를 계산
        distances = [levenshtein_distance(input_sentence, question) for question in self.questions]
        # 가장 거리가 작은 질문의 인덱스를 찾음
        best_match_index = distances.index(min(distances))
        # 가장 유사한 질문에 해당하는 답변과 인덱스를 반환
        return best_match_index, self.answers[best_match_index]

# 데이터 파일의 경로를 지정합니다.
filepath = '/content/sample_data/ChatbotData.csv'  # 업로드한 파일의 경로를 사용

# 챗봇 객체를 생성합니다.
chatbot = SimpleChatBot(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행합니다.
while True:
    # 사용자로부터 입력을 받음
    input_sentence = input('You: ')
    # 만약 사용자가 '종료'를 입력하면 루프를 종료
    if input_sentence.lower() == '종료':
        break
    # 사용자의 입력 문장에 가장 유사한 질문을 찾아 그에 해당하는 답변을 반환
    best_match_index, response = chatbot.find_best_answer(input_sentence)
    # 챗봇의 답변과 인덱스를 출력
    print(f'Chatbot: (Index: {best_match_index}) {response}')
