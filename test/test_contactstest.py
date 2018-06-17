# -*- coding: utf-8 -*-
from model.contact import Contact

def test_contactstest(app):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create_new_contact(Contact(firstname="akdjaasd",middlename="wkdjad", lastname="asdkjak", nickname="asdadad", title="aksdjakjdakdj", company="awjdkadj", address="adkadkja", home="230921301", mobile="203901313", work="19381938", fax="20391039103", email="1293193813", email2="wakda@kajd.com", email3="aodk@kajd.com", homepage="aakdakdj.com", byear="1992", ayear="2000", address2="210319301", phone2="1093109301", notes="akjdakdjakdjaldjalkdjalkdjakljdadadjadjl"))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)



