from models import Pessoas


def insere_pesssoa():
    pessoa = Pessoas(nome='Joao', idade=60)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoa_total = Pessoas.query.all()
    print(pessoa_total)
    pessoa = Pessoas.query.filter_by(nome='Heloisa').first()
    print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Heloisa').first()
    pessoa.idade = 1
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joao').first()
    pessoa.delete()
    pessoa.save()


if __name__ == '__main__':
    # insere_pesssoa()
    # altera_pessoa()
    # consulta_pessoas()
    exclui_pessoa()
