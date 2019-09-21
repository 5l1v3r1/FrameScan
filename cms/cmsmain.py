#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: cms漏洞库
referer: unknow
author: qianxiao996
description: 包含所有cms漏洞类型，封装成一个模块
此文件禁止修改
'''
#acsoft
from cms.acsoft.acsoft_GetFileContent_fileread import acsoft_GetFileContent_fileread
from cms.acsoft.acsoft_GetFile_fileread import acsoft_GetFile_fileread
from cms.acsoft.acsoft_GetXMLList_fileread import acsoft_GetXMLList_fileread

#autoset
from cms.autoset.autoset_phpmyadmin_unauth import autoset_phpmyadmin_unauth

#cmseasy
from cms.cmseasy.cmseasy_header_detail_sqli import cmseasy_header_detail_sqli

#cmsmain.py

#dedecms
from cms.dedecms.dedecms_download_redirect import dedecms_download_redirect
from cms.dedecms.dedecms_error_trace_disclosure import dedecms_error_trace_disclosure
from cms.dedecms.dedecms_recommend_sqli import dedecms_recommend_sqli
from cms.dedecms.dedecms_search_typeArr_sqli import dedecms_search_typeArr_sqli
from cms.dedecms.dedecms_version import dedecms_version

#digital_campus
from cms.digital_campus.digital_campus_log_disclosure import digital_campus_log_disclosure
from cms.digital_campus.digital_campus_systemcodelist_sqli import digital_campus_systemcodelist_sqli

#discuz
from cms.discuz.discuz_focus_flashxss import discuz_focus_flashxss
from cms.discuz.discuz_forum_message_ssrf import discuz_forum_message_ssrf
from cms.discuz.discuz_plugin_ques_sqli import discuz_plugin_ques_sqli
from cms.discuz.discuz_x25_path_disclosure import discuz_x25_path_disclosure

#diyou
from cms.diyou.dyp2p_latesindex_sqli import dyp2p_latesindex_sqli
from cms.diyou.dyp2p_url_fileread import dyp2p_url_fileread

#dreamgallery
from cms.dreamgallery.dreamgallery_album_id_sqli import dreamgallery_album_id_sqli

#dswjcms
from cms.dswjcms.dswjcms_p2p_multi_sqli import dswjcms_p2p_multi_sqli

#ecscms
from cms.ecscms.ecscms_MoreIndex_sqli import ecscms_MoreIndex_sqli

#ecshop
from cms.ecshop.ecshop_flow_orderid_sqli import ecshop_flow_orderid_sqli
from cms.ecshop.ecshop_uc_code_sqli import ecshop_uc_code_sqli
from cms.ecshop.eshop_all_code_exec import eshop_all_code_exec

#esccms
from cms.esccms.esccms_selectunitmember_unauth import esccms_selectunitmember_unauth

#etmdcp
from cms.etmdcp.etmdcp_Load_filedownload import etmdcp_Load_filedownload

#eyou
from cms.eyou.eyou_admin_id_sqli import eyou_admin_id_sqli
from cms.eyou.eyou_resetpw import eyou_resetpw
from cms.eyou.eyou_user_kw_sqli import eyou_user_kw_sqli
from cms.eyou.eyou_weakpass import eyou_weakpass

#fastmeeting
from cms.fastmeeting.fastmeeting_download_filedownload import fastmeeting_download_filedownload

#finecms
from cms.finecms.finecms_508_getshell import finecms_508_getshell
from cms.finecms.finecms_508_write_file import finecms_508_write_file
from cms.finecms.finecms_uploadfile import finecms_uploadfile

#foosun
from cms.foosun.foosun_City_ajax_sqli import foosun_City_ajax_sqli

#fsmcms
from cms.fsmcms.fsmcms_columninfo_sqli import fsmcms_columninfo_sqli
from cms.fsmcms.fsmcms_p_replydetail_sqli import fsmcms_p_replydetail_sqli
from cms.fsmcms.fsmcms_setup_reinstall import fsmcms_setup_reinstall

#gobetters
from cms.gobetters.gobetters_multi_sqli import gobetters_multi_sqli

#gowinsoft_jw
from cms.gowinsoft_jw.gowinsoft_jw_multi_sqli import gowinsoft_jw_multi_sqli

#gpower
from cms.gpower.gpower_users_disclosure import gpower_users_disclosure

#hanweb
from cms.hanweb.hanweb_downfile_filedownload import hanweb_downfile_filedownload
from cms.hanweb.hanweb_readxml_fileread import hanweb_readxml_fileread
from cms.hanweb.hanweb_VerifyCodeServlet_install import hanweb_VerifyCodeServlet_install

#Hishop
from cms.Hishop.hishop_productlist_sqli import hishop_productlist_sqli

#iGenus
from cms.iGenus.igenus_code_exec import igenus_code_exec
from cms.iGenus.igenus_login_Lang_fileread import igenus_login_Lang_fileread
from cms.iGenus.igenus_syslogin_Lang_fileread import igenus_syslogin_Lang_fileread

#inspur
from cms.inspur.inspur_ecgap_displayNewsPic_sqli import inspur_ecgap_displayNewsPic_sqli
from cms.inspur.inspur_multi_sqli import inspur_multi_sqli

#iwms
from cms.iwms.iwms_bypass_js_delete import iwms_bypass_js_delete

#jeecg
from cms.jeecg.jeecg_pwd_reset import jeecg_pwd_reset

#jeecms
from cms.jeecms.jeecms_fpath_filedownload import jeecms_fpath_filedownload

#joomla
from cms.joomla.joomla_com_docman_lfi import joomla_com_docman_lfi
from cms.joomla.joomla_index_list_sqli import joomla_index_list_sqli

#jumboecms
from cms.jumboecms.jumboecms_slide_id_sqli import jumboecms_slide_id_sqli

#kingdee
from cms.kingdee.kingdee_conf_disclosure import kingdee_conf_disclosure
from cms.kingdee.kingdee_filedownload import kingdee_filedownload
from cms.kingdee.kingdee_logoImgServlet_fileread import kingdee_logoImgServlet_fileread
from cms.kingdee.kingdee_resin_dir_path_disclosure import kingdee_resin_dir_path_disclosure

#kxmail
from cms.kxmail.kxmail_login_server_sqli import kxmail_login_server_sqli

#lbcms
from cms.lbcms.lbcms_webwsfw_bssh_sqli import lbcms_webwsfw_bssh_sqli

#libsys
from cms.libsys.libsys_ajax_asyn_link_fileread import libsys_ajax_asyn_link_fileread
from cms.libsys.libsys_ajax_asyn_link_old_fileread import libsys_ajax_asyn_link_old_fileread
from cms.libsys.libsys_ajax_get_file_fileread import libsys_ajax_get_file_fileread

#live800
from cms.live800.live800_downlog_filedownload import live800_downlog_filedownload
from cms.live800.live800_fileDownloadServer_fileread import live800_fileDownloadServer_fileread
from cms.live800.live800_loginAction_sqli import live800_loginAction_sqli
from cms.live800.live800_services_xxe import live800_services_xxe
from cms.live800.live800_sta_export_sqli import live800_sta_export_sqli

#looyu
from cms.looyu.looyu_down_filedownload import looyu_down_filedownload

#metinfo
from cms.metinfo.metinfo_getpassword_sqli import metinfo_getpassword_sqli
from cms.metinfo.metinfo_login_check_sqli import metinfo_login_check_sqli

#ndstar
from cms.ndstar.ndstar_six_sqli import ndstar_six_sqli

#nitc
from cms.nitc.nitc_index_language_id_sqli import nitc_index_language_id_sqli
from cms.nitc.nitc_suggestwordList_sqli import nitc_suggestwordList_sqli

#opensns
from cms.opensns.opensns_index_arearank import opensns_index_arearank
from cms.opensns.opensns_index_getshell import opensns_index_getshell

#others
from cms.others.alkawebs_viewnews_sqli import alkawebs_viewnews_sqli
from cms.others.anmai_grghjl_stuNo_sqli import anmai_grghjl_stuNo_sqli
from cms.others.anmai_teachingtechnology_sqli import anmai_teachingtechnology_sqli
from cms.others.caitong_multi_sleep_sqli import caitong_multi_sleep_sqli
from cms.others.caitong_multi_sqli import caitong_multi_sqli
from cms.others.cicro_DownLoad_filedownload import cicro_DownLoad_filedownload
from cms.others.clib_kindaction_fileread import clib_kindaction_fileread
from cms.others.clib_kinweblistaction_download import clib_kinweblistaction_download
from cms.others.damall_selloffer_sqli import damall_selloffer_sqli
from cms.others.dkcms_database_disclosure import dkcms_database_disclosure
from cms.others.domino_unauth import domino_unauth
from cms.others.efuture_downloadAct_filedownload import efuture_downloadAct_filedownload
from cms.others.eis_menu_left_edit_sqli import eis_menu_left_edit_sqli
from cms.others.euse_study_multi_sqli import euse_study_multi_sqli
from cms.others.gevercms_downLoadFile_filedownload import gevercms_downLoadFile_filedownload
from cms.others.gn_consulting_sqli import gn_consulting_sqli
from cms.others.gpcsoft_ewebeditor_weak import gpcsoft_ewebeditor_weak
from cms.others.gxwssb_fileDownloadmodel_download import gxwssb_fileDownloadmodel_download
from cms.others.haohan_FileDown_filedownload import haohan_FileDown_filedownload
from cms.others.hezhong_list_id_sqli import hezhong_list_id_sqli
from cms.others.hjsoft_sqli import hjsoft_sqli
from cms.others.hnkj_researchinfo_dan_sqli import hnkj_researchinfo_dan_sqli
from cms.others.hongan_dlp_struts_exec import hongan_dlp_struts_exec
from cms.others.huaficms_bypass_js import huaficms_bypass_js
from cms.others.ips_community_suite_code_exec import ips_community_suite_code_exec
from cms.others.jiuyu_library_struts_exec import jiuyu_library_struts_exec
from cms.others.jxt1039_unauth import jxt1039_unauth
from cms.others.kj65n_monitor_sqli import kj65n_monitor_sqli
from cms.others.lianbang_multi_bypass_priv import lianbang_multi_bypass_priv
from cms.others.mainone_b2b_Default_sqli import mainone_b2b_Default_sqli
from cms.others.mainone_ProductList_sqli import mainone_ProductList_sqli
from cms.others.mainone_SupplyList_sqli import mainone_SupplyList_sqli
from cms.others.mallbuilder_change_status_sqli import mallbuilder_change_status_sqli
from cms.others.mingteng_cookie_deception import mingteng_cookie_deception
from cms.others.newedos_multi_sqli import newedos_multi_sqli
from cms.others.nongyou_Item2_sqli import nongyou_Item2_sqli
from cms.others.nongyou_multi_sqli import nongyou_multi_sqli
from cms.others.nongyou_ShowLand_sqli import nongyou_ShowLand_sqli
from cms.others.nongyou_sleep_sqli import nongyou_sleep_sqli
from cms.others.rap_interface_struts_exec import rap_interface_struts_exec
from cms.others.shiyou_list_keyWords_sqli import shiyou_list_keyWords_sqli
from cms.others.sinda_downloadfile_download import sinda_downloadfile_download
from cms.others.skytech_bypass_priv import skytech_bypass_priv
from cms.others.skytech_geren_list_page_sqli import skytech_geren_list_page_sqli
from cms.others.star_PostSuggestion_sqli import star_PostSuggestion_sqli
from cms.others.suntown_upfile_fileupload import suntown_upfile_fileupload
from cms.others.tianbo_Class_Info_sqli import tianbo_Class_Info_sqli
from cms.others.tianbo_St_Info_sqli import tianbo_St_Info_sqli
from cms.others.tianbo_TCH_list_sqli import tianbo_TCH_list_sqli
from cms.others.tianbo_Type_List_sqli import tianbo_Type_List_sqli
from cms.others.tpshop_eval_stdin_code_exec import tpshop_eval_stdin_code_exec
from cms.others.workyi_multi_sqli import workyi_multi_sqli
from cms.others.xtcms_download_filedownload import xtcms_download_filedownload
from cms.others.xuezi_ceping_unauth import xuezi_ceping_unauth
from cms.others.yaojie_steel_struts_exec import yaojie_steel_struts_exec
from cms.others.yeu_disclosure_uid import yeu_disclosure_uid
from cms.others.zfcgxt_UserSecurityController_getpass import zfcgxt_UserSecurityController_getpass
from cms.others.zf_cms_FileDownload import zf_cms_FileDownload
from cms.others.zhuofan_downLoadFile_download import zhuofan_downLoadFile_download

#pageadmin
from cms.pageadmin.pageadmin_forge_viewstate import pageadmin_forge_viewstate

#php168
from cms.php168.php168_login_getshell import php168_login_getshell

#phpcms
from cms.phpcms.phpcms_authkey_disclosure import phpcms_authkey_disclosure
from cms.phpcms.phpcms_digg_add_sqli import phpcms_digg_add_sqli
from cms.phpcms.phpcms_flash_upload_sqli import phpcms_flash_upload_sqli
from cms.phpcms.phpcms_product_code_exec import phpcms_product_code_exec
from cms.phpcms.phpcms_v961_fileread import phpcms_v961_fileread
from cms.phpcms.phpcms_v96_sqli import phpcms_v96_sqli
from cms.phpcms.phpcms_v9_flash_xss import phpcms_v9_flash_xss

#phpmyadmin
from cms.phpmyadmin.phpmyadmin_setup_lfi import phpmyadmin_setup_lfi

#phpok
from cms.phpok.phpok_api_param_sqli import phpok_api_param_sqli
from cms.phpok.phpok_remote_image_getshell import phpok_remote_image_getshell
from cms.phpok.phpok_res_action_control_filedownload import phpok_res_action_control_filedownload

#phpstudy
from cms.phpstudy.phpstudy_phpmyadmin_defaultpwd import phpstudy_phpmyadmin_defaultpwd
from cms.phpstudy.phpstudy_probe import phpstudy_probe

#piaoyou
from cms.piaoyou.piaoyou_int_order_sqli import piaoyou_int_order_sqli
from cms.piaoyou.piaoyou_multi_sqli import piaoyou_multi_sqli
from cms.piaoyou.piaoyou_newsview_list import piaoyou_newsview_list
from cms.piaoyou.piaoyou_six2_sqli import piaoyou_six2_sqli
from cms.piaoyou.piaoyou_six_sqli import piaoyou_six_sqli
from cms.piaoyou.piaoyou_ten_sqli import piaoyou_ten_sqli

#PKPMBS
from cms.PKPMBS.pkpmbs_addresslist_keyword_sqli import pkpmbs_addresslist_keyword_sqli
from cms.PKPMBS.pkpmbs_guestbook_sqli import pkpmbs_guestbook_sqli
from cms.PKPMBS.pkpmbs_MsgList_sqli import pkpmbs_MsgList_sqli

#pstar
from cms.pstar.pstar_isfLclInfo_sqli import pstar_isfLclInfo_sqli
from cms.pstar.pstar_qcustoms_sqli import pstar_qcustoms_sqli
from cms.pstar.pstar_warehouse_msg_01_sqli import pstar_warehouse_msg_01_sqli

#qibocms
from cms.qibocms.qibocms_js_f_id_sqli import qibocms_js_f_id_sqli
from cms.qibocms.qibocms_search_code_exec import qibocms_search_code_exec
from cms.qibocms.qibocms_search_sqli import qibocms_search_sqli
from cms.qibocms.qibocms_s_fids_sqli import qibocms_s_fids_sqli

#ruvar
from cms.ruvar.ruvar_oa_multi_sqli import ruvar_oa_multi_sqli
from cms.ruvar.ruvar_oa_multi_sqli2 import ruvar_oa_multi_sqli2
from cms.ruvar.ruvar_oa_multi_sqli3 import ruvar_oa_multi_sqli3

#seacms
from cms.seacms.seacms_655_code_exec import seacms_655_code_exec
from cms.seacms.seacms_order_code_exec import seacms_order_code_exec
from cms.seacms.seacms_search_code_exec import seacms_search_code_exec
from cms.seacms.seacms_search_jq_code_exec import seacms_search_jq_code_exec

#shadowsit
from cms.shadowsit.shadowsit_selector_lfi import shadowsit_selector_lfi

#shop360
from cms.shop360.shop360_do_filedownload import shop360_do_filedownload

#shop7z
from cms.shop7z.shop7z_order_checknoprint_sqli import shop7z_order_checknoprint_sqli

#shopex
from cms.shopex.shopex_phpinfo_disclosure import shopex_phpinfo_disclosure

#shopnc
from cms.shopnc.shopnc_index_class_id_sqli import shopnc_index_class_id_sqli

#shopnum
from cms.shopnum.shopnum_GuidBuyList_sqli import shopnum_GuidBuyList_sqli
from cms.shopnum.shopnum_ProductDetail_sqli import shopnum_ProductDetail_sqli
from cms.shopnum.shopnum_ProductListCategory_sqli import shopnum_ProductListCategory_sqli
from cms.shopnum.shopnum_ShoppingCart1_sqli import shopnum_ShoppingCart1_sqli

#siteengine
from cms.siteengine.siteengine_comments_module_sqli import siteengine_comments_module_sqli

#siteserver
from cms.siteserver.siteserver_background_administrator_sqli import siteserver_background_administrator_sqli
from cms.siteserver.siteserver_background_keywordsFilting_sqli import siteserver_background_keywordsFilting_sqli
from cms.siteserver.siteserver_background_log_sqli import siteserver_background_log_sqli
from cms.siteserver.siteserver_background_taskLog_sqli import siteserver_background_taskLog_sqli
from cms.siteserver.siteserver_UserNameCollection_sqli import siteserver_UserNameCollection_sqli

#smartoa
from cms.smartoa.smartoa_multi_filedownload import smartoa_multi_filedownload

#speedcms
from cms.speedcms.speedcms_list_cid_sqli import speedcms_list_cid_sqli

#tcexam
from cms.tcexam.tcexam_reinstall_getshell import tcexam_reinstall_getshell

#thinkphp
from cms.thinkphp.onethink_category_sqli import onethink_category_sqli
from cms.thinkphp.thinkphp_code_exec import thinkphp_code_exec
from cms.thinkphp.thinkphp_v5x_code_exec_1 import thinkphp_v5x_code_exec_1
from cms.thinkphp.thinkphp_v5x_code_exec_2 import thinkphp_v5x_code_exec_2

#thinksns
from cms.thinksns.thinksns_category_code_exec import thinksns_category_code_exec

#trs
from cms.trs.trs_ids_auth_disclosure import trs_ids_auth_disclosure
from cms.trs.trs_infogate_register import trs_infogate_register
from cms.trs.trs_infogate_xxe import trs_infogate_xxe
from cms.trs.trs_inforadar_disclosure import trs_inforadar_disclosure
from cms.trs.trs_lunwen_papercon_sqli import trs_lunwen_papercon_sqli
from cms.trs.trs_was40_passwd_disclosure import trs_was40_passwd_disclosure
from cms.trs.trs_was40_tree_disclosure import trs_was40_tree_disclosure
from cms.trs.trs_was5_config_disclosure import trs_was5_config_disclosure
from cms.trs.trs_was5_download_templet import trs_was5_download_templet
from cms.trs.trs_wcm_default_user import trs_wcm_default_user
from cms.trs.trs_wcm_infoview_disclosure import trs_wcm_infoview_disclosure
from cms.trs.trs_wcm_pre_as_lfi import trs_wcm_pre_as_lfi
from cms.trs.trs_wcm_service_writefile import trs_wcm_service_writefile

#typecho
from cms.typecho.typecho_install_code_exec import typecho_install_code_exec

#umail
from cms.umail.umail_physical_path import umail_physical_path
from cms.umail.umail_sessionid_access import umail_sessionid_access

#uniportal
from cms.uniportal.uniportal_bypass_priv_sqli import uniportal_bypass_priv_sqli

#urp
from cms.urp.urp_query import urp_query
from cms.urp.urp_query2 import urp_query2
from cms.urp.urp_ReadJavaScriptServlet_fileread import urp_ReadJavaScriptServlet_fileread

#v2tech
from cms.v2tech.v2Conference_sqli_xxe import v2Conference_sqli_xxe

#viewgood
from cms.viewgood.viewgood_GetCaption_sqli import viewgood_GetCaption_sqli
from cms.viewgood.viewgood_pic_proxy_sqli import viewgood_pic_proxy_sqli
from cms.viewgood.viewgood_two_sqli import viewgood_two_sqli

#weaver_oa
from cms.weaver_oa.weaver_oa_db_disclosure import weaver_oa_db_disclosure
from cms.weaver_oa.weaver_oa_download_sqli import weaver_oa_download_sqli
from cms.weaver_oa.weaver_oa_filedownload import weaver_oa_filedownload

#wecenter
from cms.wecenter.wecenter_topic_id_sqli import wecenter_topic_id_sqli

#weway
from cms.weway.weway_PictureView1_filedownload import weway_PictureView1_filedownload

#wizbank
from cms.wizbank.wizbank_download_filedownload import wizbank_download_filedownload
from cms.wizbank.wizbank_usr_id_sqli import wizbank_usr_id_sqli

#wordpress
from cms.wordpress.wordpress_admin_ajax_filedownload import wordpress_admin_ajax_filedownload
from cms.wordpress.wordpress_display_widgets_backdoor import wordpress_display_widgets_backdoor
from cms.wordpress.wordpress_plugin_azonpop_sqli import wordpress_plugin_azonpop_sqli
from cms.wordpress.wordpress_plugin_mailpress_rce import wordpress_plugin_mailpress_rce
from cms.wordpress.wordpress_plugin_ShortCode_lfi import wordpress_plugin_ShortCode_lfi
from cms.wordpress.wordpress_restapi_sqli import wordpress_restapi_sqli
from cms.wordpress.wordpress_url_redirect import wordpress_url_redirect
from cms.wordpress.wordpress_woocommerce_code_exec import wordpress_woocommerce_code_exec

#xplus
from cms.xplus.xplus_2003_getshell import xplus_2003_getshell
from cms.xplus.xplus_mysql_mssql_sqli import xplus_mysql_mssql_sqli

#yonyou
from cms.yonyou.yonyou_a8_CmxUser_sqli import yonyou_a8_CmxUser_sqli
from cms.yonyou.yonyou_a8_logs_disclosure import yonyou_a8_logs_disclosure
from cms.yonyou.yonyou_a8_personService_xxe import yonyou_a8_personService_xxe
from cms.yonyou.yonyou_cm_info_content_sqli import yonyou_cm_info_content_sqli
from cms.yonyou.yonyou_createMysql_disclosure import yonyou_createMysql_disclosure
from cms.yonyou.yonyou_ehr_ELTextFile import yonyou_ehr_ELTextFile
from cms.yonyou.yonyou_ehr_resetpwd_sqli import yonyou_ehr_resetpwd_sqli
from cms.yonyou.yonyou_fe_treeXml_sqli import yonyou_fe_treeXml_sqli
from cms.yonyou.yonyou_getemaildata_fileread import yonyou_getemaildata_fileread
from cms.yonyou.yonyou_icc_struts2 import yonyou_icc_struts2
from cms.yonyou.yonyou_initData_disclosure import yonyou_initData_disclosure
from cms.yonyou.yonyou_multi_union_sqli import yonyou_multi_union_sqli
from cms.yonyou.yonyou_nc_NCFindWeb_fileread import yonyou_nc_NCFindWeb_fileread
from cms.yonyou.yonyou_status_default_pwd import yonyou_status_default_pwd
from cms.yonyou.yonyou_test_sqli import yonyou_test_sqli
from cms.yonyou.yonyou_u8_CmxItem_sqli import yonyou_u8_CmxItem_sqli
from cms.yonyou.yonyou_user_ids_sqli import yonyou_user_ids_sqli

#zfsoft
from cms.zfsoft.zfsoft_database_control import zfsoft_database_control
from cms.zfsoft.zfsoft_default3_bruteforce import zfsoft_default3_bruteforce
from cms.zfsoft.zfsoft_service_stryhm_sqli import zfsoft_service_stryhm_sqli

#zuitu
from cms.zuitu.zuitu_coupon_id_sqli import zuitu_coupon_id_sqli

#__pycache__

