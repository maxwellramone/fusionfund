#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion_fund.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()






def getContent(url):
	import requests
	from bs4 import BeautifulSoup
	content = ""
	url = 'https://www.ft.com/content/4c64ffc1-f57b-4e22-a4a5-f9f90a7419b7'

	try:
		response = requests.get(url)
		response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, 'html.parser')
			
			# article_titles = soup.find_all('title', class_='html.parser')  # Use a dictionary for attributes
			article_paragraphs = soup.find_all('p')
			for paragraph in article_paragraphs:
				content.append(paragraph)
			return content
		else:
			print('Failed. Code:', response.status_code)
		

	except requests.exceptions.RequestException as e:
		print('Request Exception:', e)

	except Exception as e:
		print('An error occurred:', e)

	return