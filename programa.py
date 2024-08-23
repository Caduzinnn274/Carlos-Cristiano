import os
from Contato import Restaurante

class ProgramaExpresso:
    def __init__(self):
        self.restaurantes = [
            Restaurante('Carlos', '41 99770-0907', True),
            Restaurante('Cristiano', '41 98714-9913', True),
            
        ]

    def finalizar_app(self):
        os.system("clear")
        os.system("cls")
        print("Finalizando o app\n")

    def voltar_menu_principal(self):
        input("Digite uma tecla para voltar ao menu principal: ")

    def mostrar_subtitulo(self, texto):
        os.system("clear")
        linha = '*'*(len(texto))
        print(linha)
        print(texto)
        print(linha)
        print()

    def escolher_opcoes(self):
        self.mostrar_subtitulo("Contact Manager\n".ljust(20))
        
        print("1 - Cadastrar Contatos")
        print("2 - Listar Contatos")
        print("3 - Ativar/Desativar Contato")
        print("4 - Sair\n")

    def opcao_invalida(self):
        self.mostrar_subtitulo("Opção inválida\n".ljust(20))
        self.voltar_menu_principal()

    def listarContatos(self):
        self.mostrar_subtitulo('Listando os Contatos'.ljust(20))
        print("Nome:".ljust(27), "Número:".ljust(34), "Status:".ljust(24))
        for contato in self.restaurantes:
            print(contato)

    def alternar_estado_contato(self):
        self.mostrar_subtitulo("Alterando o status do contato".ljust(20))
        self.listarContatos()
        nome_contato = input("Digite o nome do Contato que desejas alterar: ")
        contato_encontrado = False

        for contato in self.restaurantes:
            if nome_contato == contato.nome:
                contato_encontrado = True
                mensagem = contato.ativar_desativar()
                print(mensagem)
                break

        if not contato_encontrado:
            print("O Contato não foi encontrado.")

        self.voltar_menu_principal()

    def cadastrar_novo_contato(self):
        nome_do_contato = input("Digite o nome do novo contato: ")
        numero = input(f'Digite o número do contato {nome_do_contato}: ')
        contato_novo = Restaurante(nome_do_contato, numero)
        self.restaurantes.append(contato_novo)
        print(f"Você cadastrou o restaurante: {nome_do_contato}")

    def main(self):
        while True:
            try:
                self.escolher_opcoes()
                opcao_digitada = int(input("Digite a opção desejada: "))
                if opcao_digitada == 1:
                    print("Você escolheu cadastrar novo contato\n" )
                    self.cadastrar_novo_contato()
                elif opcao_digitada == 2:
                    self.listarContatos()
                    self.voltar_menu_principal()
                elif opcao_digitada == 3:
                    self.alternar_estado_contato()
                elif opcao_digitada == 4:
                    print("Você escolheu sair do aplicativo\n")
                    self.finalizar_app()
                    break
                else:
                    self.opcao_invalida()
            except ValueError:
                print("Por favor, digite um número válido.")

if __name__ == "__main__":
    programa = ProgramaExpresso()
    programa.main()
