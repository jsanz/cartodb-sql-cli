from cartodb import CartoDBAPIKey, CartoDBException
import click

class CartoDBUser(object):
    def __init__(self, user_name=None, api_key=None):
        self.client = CartoDBAPIKey(api_key, user_name)
        self.user_name = user_name

@click.group()
@click.option('--user-name', help='Your CartoDB user')
@click.option('--api-key',
    help='API KEY, you can use also the env var CARTODB_API_KEY')
@click.pass_context
def cli(ctx, user_name, api_key):
    ctx.obj = CartoDBUser(user_name, api_key)


@click.command(help="Gets the number of records of a table")
@click.argument('table_name')
@click.pass_obj
def count(cartodb, table_name):
    try:
        response = cartodb.client.sql(
            'select count(*) from {}'.format(table_name))
        rows = response.get('rows')
        count = rows[0].get('count')
        click.echo(count)
    except CartoDBException as e:
        print("some error ocurred", e)


@click.command(help='Gets the BBOX of a table')
@click.argument('table_name')
@click.pass_obj
def bbox(cartodb, table_name):
    try:
        response = cartodb.client.sql(
            '''
            with data as (select ST_Extent(the_geom) as bbox from {} )
            select
                ST_XMax(bbox) xmax, ST_XMin(bbox) xmin,
                ST_YMax(bbox) ymax, ST_YMin(bbox) ymin
            from data'''.format(table_name))
        rows = response.get('rows')
        xmax = rows[0].get('xmax')
        ymax = rows[0].get('ymax')
        xmin = rows[0].get('xmin')
        ymin = rows[0].get('ymin')
        click.echo("SW: {:+9.4f} | {:+9.4f}".format(xmin, ymin))
        click.echo("NE: {:+9.4f} | {:+9.4f}".format(xmax, ymax))
    except CartoDBException as e:
        print("some error ocurred", e)


@click.command(help='List schemas')
@click.pass_obj
def schema_list(cartodb):
    try:
        response = cartodb.client.sql('''
            select nspname as user
            from pg_catalog.pg_namespace
            where not nspowner = 10 order by nspname
            ''')
        rows = response.get('rows')
        for row in rows:
            click.echo(row.get('user'))
    except CartoDBException as e:
        print("some error ocurred", e)


@click.command(help='List users tables')
@click.pass_obj
def table_list(cartodb):
    try:
        response = cartodb.client.sql('''
            select table_name
            from information_schema.tables
            where table_schema in (\'public\',\'{}\')
            order by table_name
            '''.format(cartodb.user_name))
        rows = response.get('rows')
        for row in rows:
            click.echo(row.get('table_name'))
    except CartoDBException as e:
        print("some error ocurred", e)

cli.add_command(count)
cli.add_command(bbox)
cli.add_command(table_list)
cli.add_command(schema_list)

if __name__ == '__main__':
    # Use environment variables starting as CARTODB
    cli(auto_envvar_prefix='CARTODB')
