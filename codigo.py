import os
import getpass

class CaronaUnimar:
    def cadastrar(self) -> None:
        with open('usuarios.txt', 'a') as file:
            user = input('Nome do usuário: ')
            passwd = getpass.getpass('Senha do usuário: ')
            file.write(f'{user}:{passwd}\n')

    def login(self, user, passwd) -> bool:
        with open('usuarios.txt', 'r') as file:
            for row in file:
                if user in row:
                    senha_user = str(row[row.index(':')+1:]).strip()
                    if passwd == senha_user:
                        return True
            return False
        
    def listar(self) -> None:
        with open('usuarios.txt', 'a') as file:
            file.write('carona unimar\n')
        
        with open('usuarios.txt', 'r') as file:
            print('--lista de usuarios--')
            print(file.read())
        
        input('aperte enter para continuar')

    def exibir_menu(self):
        menu = """\t--Bem vindo--
        [1] Cadastrar
        [2] Login
        [3] Listar
        [4] Sair
        Opção: """
        opcao = input(menu)
        return opcao

    def carona_unimar(self):
        print("Carona Unimar")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.exibir_menu()
            os.system('cls' if os.name == 'nt' else 'clear')

            if opcao == '1':
                self.cadastrar()
            elif opcao == '2':
                user = input('Usuário: ')
                passwd = getpass.getpass('Senha: ')
                if self.login(user, passwd):
                    print(f'Entrou com sucesso na conta {user}')
                else:
                    print('Senha ou Usuário incorreto(s)')
                    input('Pressione enter para continuar')
            elif opcao == '3':
                print("Para acessar esta aba voce precisa da senha do administrador")
                senha_adm = int(input("Qual a senha do administrador? "))
                if senha_adm == 123456789:
                    self.listar()
                else:
                  print("!!!acesso negado!!!")
            elif opcao == '4':
                break

if __name__ == '__main__':
    carona = CaronaUnimar()
    carona.carona_unimar()
