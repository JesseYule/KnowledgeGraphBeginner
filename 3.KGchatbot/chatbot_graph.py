from question_classifier import *
from question_parser import *
from answer_search import *


'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您好，我是医药智能助理Homunculus。'
        res_classify = self.classifier.classify(sent)

        # 对问题进行分类，不过问题不属于该领域，则直接回复默认回答
        # 分类的结果其实就是分析问题的实体以及问题的类型，比如{感冒，感冒的描述}、{咳嗽，咳嗽可能涉及到什么疾病}
        # 本质上就是分析出有没有涉及到Neo4j中的node、property、relationship

        print(res_classify)

        if not res_classify:
            return answer

        # 对问题的分类结果进行进一步的解析
        # 其实就是生成sql语句，根据node、property、relationship在数据库中查找相关信息
        res_sql = self.parser.parser_main(res_classify)

        print(res_sql)

        final_answers = self.searcher.search_main(res_sql)

        print(final_answers)

        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('用户:')
        answer = handler.chat_main(question)
        print('Homunculus:', answer)

