# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-12-28 22:22

from hanlp.components.tok_tf import TransformerTokenizerTF
from hanlp.datasets.cws.ctb import CTB6_CWS_TRAIN, CTB6_CWS_DEV, CTB6_CWS_TEST
from tests import cdroot

cdroot()
tokenizer = TransformerTokenizerTF()
save_dir = 'data/model/cws_bert_base_ctb6'
# tagger.fit(CTB6_CWS_TRAIN, CTB6_CWS_DEV, save_dir, transformer='bert-base-chinese',
#               metrics='f1')
tokenizer.load(save_dir)
print(tokenizer.predict(['中央民族乐团离开北京前往维也纳', '商品和服务']))
tokenizer.evaluate(CTB6_CWS_TEST, save_dir=save_dir)
print(f'Model saved in {save_dir}')
