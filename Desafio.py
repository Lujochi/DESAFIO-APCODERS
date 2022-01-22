import mysql.connector
from menus import (menu_sec,menu_principal,menu_verf,menu_terc,menu_dep,filtro,dep)

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    database = 'desafio',
    passwd = ''
)

cursor = mydb.cursor()

def main():
    menu_principal()
    op = int(input('-> Opção: '))

    if op == 1:
        menu_sec()
        op = int(input('-> Opção: '))
        if op == 1:
            print('-> Preencha os dados solicitados abaixo.')
            nome = input('Nome: ')
            Dnasci = input('Data de nascimento aaaa/mm/dd: ')
            sexo = input('[M]Masculino [F]Feminino: ')
            telef = input('Telefone: ')
            email = input('Email: ')
            sql = 'INSERT INTO inquilinos (nome,data_nascimento,sexo,telefone,email) VALUES('
            valores = ('\'' +nome+ '\',' + '\'' + Dnasci + '\',' + '\'' + sexo + '\',' + '\'' +telef +'\',' + '\''+email+'\'' + ')')
            cursor.execute(sql + valores)
            mydb.commit()
            print(cursor.rowcount,'Registros adicionados! ')
            menu_verf()
            op = input('-> Opção: ')
            if op == 1:
               main()
            else:
                main()

        if op == 2:
            cursor.execute('select i.id,i.nome,i.data_nascimento,i.sexo,i.telefone,i.email,u.Condomínio from inquilinos as i left outer join unidades as u on  u.id = i.Condominio order by i.nome')
            linhas = cursor.fetchall()
            print('Número total de registros:', cursor.rowcount)
            print('''\nInquilinos cadastrados:
            ''')
            for linha in linhas:
                print('-'*30)
                print('Id:',linha[0])
                print('Nome:',linha[1])
                print('Data de nascimento:',linha[2])
                print('Sexo:',linha[3])
                print('Telefone:',linha[4])
                print('Email:',linha[5])
                print('Condomínio:',linha[6])
            menu_verf()
            op = input('-> Opção: ')
            if op == 1:
                main()
            else:
                main()
        else:
            print('Erro! Opção digitada não existe!')
            menu_verf()
            op = input('-> Opção: ')
            if op == 1:
                main()
            else:
                main()

    if op == 2:
        menu_terc()
        op = int(input('-> Opção: '))
        if op == 1:
            print('-> Preencha os dados solicitados abaixo.')
            prop = input('Proprietario: ')
            cond = input('Condominio: ')
            end = input('Endereço: ')
            cmand = 'INSERT INTO unidades (Proprietário,Condomínio,Endereço) VALUES ('
            conkat = ('\'' + prop + '\',' + '\'' + cond + '\',' + '\'' + end + '\'' + ')')
            cursor.execute(cmand + conkat)
            mydb.commit()
            print(cursor.rowcount,'Registros adicionados!')
            menu_verf()
            op = input('-> Opção: ')
            if op == 1:
                main()
            else:
                main()
        
        if op == 2:
            cursor.execute('select u.id,u.Proprietário,u.Condomínio,u.Endereço,d.valor from unidades as u left outer join despesas_unidades as d on d.id = u.despesas_das_unidades order by u.Proprietário')
            linhas = cursor.fetchall()
            print('Número total de registros:', cursor.rowcount)
            print('''\nUnidades cadastrados:
            ''')
            for linha in linhas:
                print('-'*30)
                print('Id:',linha[0])
                print('Proprietario:',linha[1])
                print('Condominio:',linha[2])
                print('Endereço:',linha[3])
                print('Despesa da unidade',linha[4])
            menu_verf()
            op = input('-> Opção: ')
            if op == 1:
                main()
            else:
                main()
        
        if op == 3:
            menu_dep()
            op = int(input('-> Opção: '))
            if op == 1:
                print('-> Preencha os dados solicitados abaixo.')
                Desc = input('Descrição: ')
                Tipo = input('Tipo da despesa: ')
                Valor = input('Valor: ')
                Valid = input('Vencimento da fatura: ')
                status = input('Status do pagamento: ')
                comand = 'INSERT INTO despesas_unidades (descrição,tipo_despesa,valor,vencimento_fatura,status_pagamento) VALUES ('
                conca = ('\'' + Desc + '\',' + '\'' + Tipo + '\',' + '\'' + Valor + '\',' + '\'' + Valid + '\',' + '\'' + status + '\'' + ')')
                cursor.execute(comand + conca)
                mydb.commit()
                print(cursor.rowcount,'Registros adicionados!')
                menu_verf()
                op = input('-> Opção: ')
                if op == 1:
                    main()
                else:
                    main()
            if op == 2:
                dep()
                op = int(input('-> Opção: '))
                if op == 1:
                    id_desp = input('Digite o id da despesa: ')
                    Nvalor = input('Digite o novo valor: ')
                    sql = 'UPDATE desafio.despesas_unidades SET valor = %s WHERE id = %s' % (Nvalor,id_desp)
                    cursor.execute(sql)
                    print('Registro alterado com sucesso!')
                    menu_verf()
                    op = input('-> Opção: ')
                    if op == 1:
                        main()
                    else:
                        main()

                if op == 2:
                    Excl = input('Digite o id da dispesa que deseja excluir: ')
                    sql = 'DELETE FROM despesas_unidades WHERE id = %s' % (Excl)
                    cursor.execute(sql)
                    print('Registro apagado com sucesso! ')
                    menu_verf()
                    op = input('-> Opção: ')
                    if op == 1:
                        main()
                    else:
                        main()

            if op == 3:
                filtro()
                op = int(input('-> Opção: '))
                if op == 1:
                    cursor.execute('select * from despesas_unidades order by descrição')
                    linhas = cursor.fetchall()
                    print('Número total de registros:', cursor.rowcount)
                    print('''\nDespesas cadastradas:
                    ''')
                    for linha in linhas:
                        print('-'*30)
                        print('Id:',linha[0])
                        print('Descrição:',linha[1])
                        print('Tipo de despesa:',linha[2])
                        print('Valor:',linha[3])
                        print('Vencimento da fatura:',linha[4])
                        print('Status do pagamento',linha[5])
                    menu_verf()
                    op = input('-> Opção: ')
                    if op == 1:
                        main()
                    else:
                        main()

                if op == 2:
                    quest = input('Qual 0 id da unidade que deseja procurar: ')
                    sql = 'select * from despesas_unidades where id = %s' % (quest)
                    cursor.execute(sql) 
                    linhas = cursor.fetchall()
                    print('Número total de registros:', cursor.rowcount)
                    print('''\nDespesas cadastradas:
                    ''')
                    for linha in linhas:
                        print('-'*30)
                        print('Id:',linha[0])
                        print('Descrição:',linha[1])
                        print('Tipo de despesa:',linha[2])
                        print('Valor:',linha[3])
                        print('Vencimento da fatura:',linha[4])
                        print('Status do pagamento',linha[5])
                    menu_verf()
                    op = input('-> Opção: ')
                    if op == 1:
                        main()
                    else:
                        main()

                if op == 3:
                    concac = ('\'' + 'vencida' + '\'')
                    sql = 'SELECT * FROM despesas_unidades WHERE status_pagamento = %s order by descrição' % (concac)
                    cursor.execute(sql)
                    linhas = cursor.fetchall()
                    print('Número total de registros:', cursor.rowcount)
                    print('''\nDespesas cadastradas com fatura vencida:
                    ''')
                    for linha in linhas:
                        print('-'*30)
                        print('Id:',linha[0])
                        print('Descrição:',linha[1])
                        print('Tipo de despesa:',linha[2])
                        print('Valor:',linha[3])
                        print('Vencimento da fatura:',linha[4])
                        print('Status do pagamento',linha[5])
                    menu_verf()
                    op = input('-> Opção: ')
                    if op == 1:
                        main()
                    else:
                        main()                                        

                else:
                    print('Erro! Opção digitada não existe!')
                    menu_verf()
                    op = input('-> Opção: ')
                    if op == 1:
                        main()
                    else:
                        main()

            if op == 4:
                id_d = input('Digite o id da despesa: ')
                id_u = input('Digite o id da unidade: ')
                sql = 'UPDATE desafio.unidades SET despesas_das_unidades = %s WHERE id = %s' %(id_d,id_u)
                cursor.execute(sql)
                print('Despesa cadastrada na unidade!')
                menu_verf()
                op = input('-> Opção: ')
                if op == 1:
                    main()
                else:
                    main()

            else:
                print('Erro! Opção digitada não existe!')
                menu_verf()
                op = input('-> Opção: ')
                if op == 1:
                    main()
                else:
                    main()

        else:
            print('Erro! Opção digitada não existe!')
            menu_verf()
            op = input('-> Opção: ')
            if op == 1:
                main()
            else:
                main()
    
    if op == 3:
        Inq = int(input('Digite o Id do inquilino: '))
        Unid = int(input('Digite o id da unidade: '))
        upd = 'UPDATE inquilinos SET Condominio = %s WHERE id = %s;' % (Unid,Inq)
        cursor.execute(upd)
        print('Inquilino cadastrado!')
        menu_verf()
        op = input('-> Opção: ')
        if op == 1:
            main()
        else:
            main()

    else:
        print('Erro! Opção digitada não existe!')
        menu_verf()
        op = input('-> Opção: ')
        if op == 1:
            main()
        else:
            main()
main()
