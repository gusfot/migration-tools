import click
import excel2mysql as xm


@click.group()
def cli1():
    pass


@cli1.command("mig")
@click.option('-f', 'filename', required=True, multiple=False, help='파일전체경로')
@click.option('-t', 'truncate', required=False, is_flag=True, default=False, help='테이블비우기')
@click.option('-c', 'create_table', required=False, is_flag=True, default=False, help='테이블생성하기')
@click.option('-n', 'table_name', required=False, is_flag=False, default='', help='테이블명, 기존테이블명이 아닌경우 -c 옵션과 같이 사용한다.')
def migrate(filename, truncate, create_table, table_name):
    xm.migrate(filename, truncate, create_table, table_name)


cli = click.CommandCollection(sources=[cli1])

if __name__ == '__main__':
    cli()