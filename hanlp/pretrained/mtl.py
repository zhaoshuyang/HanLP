# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-12-22 13:16
from hanlp_common.constant import HANLP_URL

OPEN_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH = HANLP_URL + 'mtl/open_tok_pos_ner_srl_dep_sdp_con_electra_small_20201223_035557.zip'
"Electra small version of joint tok, pos, ner, srl, dep, sdp and con model trained on open-source Chinese corpus."
OPEN_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH = HANLP_URL + 'mtl/open_tok_pos_ner_srl_dep_sdp_con_electra_base_20201223_201906.zip'
"Electra base version of joint tok, pos, ner, srl, dep, sdp and con model trained on open-source Chinese corpus."
CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH = HANLP_URL + 'mtl/close_tok_pos_ner_srl_dep_sdp_con_electra_small_zh_20201222_130611.zip'
"Electra small version of joint tok, pos, ner, srl, dep, sdp and con model trained on private Chinese corpus."
CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH = HANLP_URL + 'mtl/close_tok_pos_ner_srl_dep_sdp_con_electra_base_20201226_221208.zip'
"Electra base version of joint tok, pos, ner, srl, dep, sdp and con model trained on private Chinese corpus."

UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_MT5_SMALL = HANLP_URL + 'mtl/ud_ontonotes_tok_pos_lem_fea_ner_srl_dep_sdp_con_mt5_small_20201231_211858.zip'
'mt5 small version of joint tok, pos, lem, fea, ner, srl, dep, sdp and con model trained on UD and OntoNotes5 corpus.'

UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_XLMR_BASE = HANLP_URL + 'mtl/ud_ontonotes_tok_pos_lem_fea_ner_srl_dep_sdp_con_xlm_base_20210104_153159.zip'
'XLM-R base version of joint tok, pos, lem, fea, ner, srl, dep, sdp and con model trained on UD and OntoNotes5 corpus.'

# Will be filled up during runtime
ALL = {}
