"""资料与现有领域接口的核对。"""
import unittest,tempfile,json
from pathlib import Path
from lake.storage import Storage
from lake.dictionary import inspect

class DomainTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name);self.store=Storage(self.root/'objects')
        self.data=json.loads(Path('data/source.json').read_text(encoding='utf-8'))
    def test_existing_reader(self):
        self.assertTrue(inspect(self.data,self.store,self.root))

    def test_null_code_not_dereferenced(self):
        from lake.dictionary import decode
        b=self.data['blocks'][0];self.assertEqual(decode(b),['HKG','SHA','HKG',None])
        with self.assertRaises(ValueError):decode(dict(b,valid=[True]*4))
