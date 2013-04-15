def vacancies_by_manager(handler, employer_manager_id):
    def vacancy_list_callback(xml, response):
        if response.code == 403:
            raise HTTPError(403)
        if xml is None:
            raise HTTPError(503)
        vacancy_ids = xml.xpath('//vacancy/@id')
        if vacancy_ids:
            self.doc.put(Element('some'), highlight =
                handler.config.vacancies_prolongate_highlight)
    url = "{host}employerManager/"+
    "{employer_manager_id}/vacancies".format(
        host = handler.config.serviceHost,
        employer_manager_id = employer_manager_id)
    handler.get_url(url, data =
                    {'userId' : handler.session.user_id},
                    callback = vacancy_list_callback)

