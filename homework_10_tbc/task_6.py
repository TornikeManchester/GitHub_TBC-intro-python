def analysis(**kwargs):
    company_name = kwargs.get("company_name", "unknown")
    release_year = kwargs.get("release_year", "unknown")
    print(f'Name: {company_name}, Release year: {release_year}')

