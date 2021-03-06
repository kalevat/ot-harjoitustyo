from invoke import task


@task
def start(ctx):
    print("""
    Ohjelma tulee käynnistää poetry run python3 src/index.py käskyllä. 
    Komento poetry run invoke start ei toimi kunnolla, kun käyttäjä antaa syötteitä.
    """
    ) 
    ctx.run("python3 src/index.py")


@task
def test(ctx):
    ctx.run("pytest src")


@task
def build(ctx):
    ctx.run("python3 src/build.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")