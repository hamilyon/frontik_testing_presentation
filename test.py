class TestEmployerVacanciesPage(TestCase):
    def setUp(self,):
        self.employer_manager_id = '3'

    def test_vacancies_by_manager(self,):
        env = EmptyEnvironment()
        set_up_service_host_mocks(env)
        set_up_negotiation_host_mocks(env)
        doc = env.do(loginAsEmployer).configure(
            vacancies_prolongate_highlight = 3
        ).call(
            vacancies_by_manager,
            employer_manager_id=self.employer_manager_id,
            sort_order='BY_ARCHIVATION_TIME_ASC').get_doc().root_node # or get_result()

        #pretty_print_xml(doc)

        em_id_actual = doc.xpath('//vacancyInternalInfo/ownerEmployerManagerId/text()')[0]
        self.assertEqual(em_id_actual, self.employer_manager_id)

