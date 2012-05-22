self.register(SofeaEmployerMock())
self.execute_async_method(
    self.handler, vacancy_list_page_by_manager, '3', '1')
doc = self.handler.doc.root_node
self.assertEqual(
    doc.xpath(
        '//employer/employerManager/fullName/text()')[0],
                 u'Evreni Petrovich')
self.assertEqual(
    doc.xpath(
        '//employer/@id')[0], '1')
self.assertEqual(
    doc.xpath(
        '//employer/russia/text()')[0], 'true')
