#!/usr/bin/env python3
# coding:utf-8
import random
import sys
import threading
import urllib
from urllib.parse import urlparse
import mechanize
from bs4 import BeautifulSoup
import requests


class WebScanner:

    def __init__(self, url, proxy=None, user_agent="Mozilla/5.0 (X11; Linux i686; rv:68.0)\
     Gecko/20100101 Firefox/68.0"):
        if not url.endswith("/") and not url.endswith(".php") and not url.endswith(".html"):
            self.url = url + "/"
        else:
            self.url = url
        self.proxy = proxy
        self.user_agent = user_agent
        self.browser = mechanize.Browser()
        self.link_list = []
        self.stopped = False

    def print_link_list(self):
        """
        Affiche la liste de liens ("crawlés") dans le Terminal
        :return:
        """
        for link in self.link_list:
            print(link)

    def get_page_source(self, page=None):
        """
        Obtient le code source d'une page web
        :param page: optionnel : la page recherchée, sinon utilise self.url
        :return: Le code source HTML de la page
        """
        if page is None:
            page = self.url
        self.browser.set_handle_robots(False)
        user_agent = {("User-agent", self.user_agent)}
        self.browser.addheaders = user_agent
        if self.proxy:
            self.browser.set_proxies(self.proxy)
        page = page.strip()
        try:
            res = self.browser.open(page)
        except Exception as e:
            print("[-] Erreur pour la page : " + page + " " + str(e))
            return None
        return res

    def get_page_links(self, page=None):
        """
        Obtient les liens disponibles sur une page web (href), excluant les liens externes
        :param page: la page recherchée, sinon utilise self.url
        :return: une liste contenant les liens d'une page, ou une liste vide à défaut
        """
        link_list = []  # la liste de liens internes à "page"

        if page is None:
            page = self.url
        source = self.get_page_source(page)

        if source is not None:
            soup = BeautifulSoup(source, "html.parser")
            uparse = urlparse(page)
            for link in soup.find_all("a"):
                if not link.get("href") is None:
                    href = link.get("href")
                    if "#" in href:
                        href = href.split("#")[0]
                    new_link = urllib.parse.urljoin(page, href)
                    if uparse.hostname in new_link and new_link not in link_list:
                        link_list.append(new_link)
            return link_list
        else:
            return []

    def print_cookies(self):
        """
        Affiche les cookies de la session courante dans le Terminal
        :return:
        """
        for cookie in self.browser.cookiejar:
            print(cookie)

    def get_cookies(self):
        """
        Retourne la liste des cookies de la session courante
        :return: La liste (dictionnaire) des cookies
        """
        return self.browser.cookiejar

    def _do_crawl(self, queue, page=None):
        """
        Crawl (indexe) une page de manière récursive en arrière-plan
        :param page: la page recherchée, sinon utilise self.url
        :return:
        """
        try:
            page_links = self.get_page_links(page)
            for link in page_links:
                if self.stopped:
                    break
                if link not in self.link_list:
                    self.link_list.append(link)
                    # print("Lien ajouté à la liste : " + link)
                    queue.put(link)
                    self._do_crawl(queue, link)
        except KeyboardInterrupt:
            print("\nProgramme arrêté par l'utilisateur")
            sys.exit(1)
        except Exception as e:
            print("\nErreur : " + str(e))
            sys.exit(2)

    def _crawl_end_callback(self, crawl_thread, crawl_queue):
        """
        Tâche d'arrière-plan pour envoyer le message de fin de crawling
        :param crawl_thread: Le thread à observer
        :param crawl_queue: La queue à utiliser pour les communications
        :return:
        """
        crawl_thread.join()
        crawl_queue.put("END")

    def crawl(self, crawl_queue, page=None):
        crawl_thread = threading.Thread(target=self._do_crawl, args=(crawl_queue, page))
        crawl_thread.start()
        thread2 = threading.Thread(target=self._crawl_end_callback, args=(crawl_thread, crawl_queue))
        thread2.start()

    def check_sqli(self, page=None):
        """
        Chercher des vulnérabilités par injection SQL dans un forumulaire
        :param page: la page recherchée, sinon utilise self.url
        :return:
        """
        if page is None:
            page = self.url
        source = self.get_page_source(page)
        if source is not None:
            soup = BeautifulSoup(source, "html.parser")
            forms_list = soup.find_all("form")

            payload = "'" + random.choice("abcdef")
            ret = ""
            for form in forms_list:
                form_action = form.get("action")
                form_method = form.get("method")
                target_url = urllib.parse.urljoin(page, form_action)

                input_list = form.find_all("input")
                param_list = {}

                for input_ in input_list:
                    input_name = input_.get("name")
                    input_type = input_.get("type")
                    input_value = input_.get("value")

                    if "?" + input_name not in target_url and "&" + input_name not in target_url:
                        if input_type == "text" or input_type == "password":
                            param_list[input_name] = payload
                        elif input_value is not None:
                            param_list[input_name] = input_value
                        else:
                            param_list[input_name] = ""

                    if form_method.lower() == "get":
                        res = requests.get(target_url, params=param_list)

                    elif form_method.lower() == "post":
                        res = requests.post(target_url, data=param_list)

                    if "You have an error in your SQL syntax;" in res.text:
                        print("INJECTION SQL DETECTEE DANS FORM : " + res.url + " (" + form_action + ")")
                        ret = ret + "INJECTION SQL DETECTEE DANS FORM : " + res.url + " (" + form_action + ")\n"

            return ret
