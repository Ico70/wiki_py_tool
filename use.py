@app.command()
def main(page: Optional[str] = typer.Option(None, "--page", help="Page to search for"),
         language: Optional[str] = typer.Option(None, "--language", help="Language to use"),
         download_pdf: bool = typer.Option(False, "--download-pdf", help="Download as PDF"),
         email: Optional[str] = typer.Option(None, "--email", help="Email to send to")):
    if page:
        typer.echo(f"Searching for page: {page}")
    if language:
        typer.echo(f"Setting language to: {language}")
    if download_pdf:
        typer.echo("Downloading page as PDF")
    if email:
        typer.echo(f"Sending email to: {email}")