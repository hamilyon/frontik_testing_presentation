class TestEmployerVacanciesPage(TestCase):
    def test_vacancies_by_manager(self,):
        env = EmptyEnvironment()
        set_stub(env, favorite_vacancies,
            'serviceHost/ManagerVacancies.xml')
        doc = env.configure(
            vacancies_prolongate_highlight = 3
        ).call(
            vacancies_by_manager,
            employer_manager_id='3',
        ).get_doc().root_node # or get_result()
        em_id_actual = doc.xpath('//some/xPath/[0]')
        self.assertEqual(em_id_actual, '3')

