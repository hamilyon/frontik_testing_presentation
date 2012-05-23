self.register(SofeaEmployerMock())
self.execute_async_method(
    self.handler, vacancy_list_page_by_manager, '3', '1')
doc = self.handler.doc.root_node
self.assertEqual(
    doc.findtext('vacancy/vacancyId'), '1')
self.assertEqual(
    doc.findtext('company/id'), '63357')
self.assertEqual(
    doc.findtext('company/name/'), 'PROFPARK, ZAO')
