    def test_save_method(self):
        self.instance.save()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)

        self.assertIn(self.key, saved_data)
        self.assertEqual(saved_data[self.key], self.new_model.to_dict())

    def test_reload_method(self):
        self.instance.save()
        self.instance.reload()

        with open(self.file_path, 'r') as file:
            reloaded_data = json.load(file)

        self.assertIn(self.key, reloaded_data)
        self.assertEqual(reloaded_data[self.key], self.new_model.to_dict())
