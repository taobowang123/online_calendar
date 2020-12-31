//Sets values of the editModal and opens the modal view
function editModal(eventid, event) {
    $('#eventttID').val(eventid);
    $('#editEventtitle').val(event);
};

//Sets the values of the settingsModal and opens the modal view
function settingsModal(fname, sname, username) {
    $('.modal-body #settingsFName').val(fname);
    $('.modal-body #settingsSName').val(sname);
    $('.modal-body #settingsEmail').val(username);

};


//Sets values of the shareModal and opens the modal view
function shareModal(id, date, title, starttime, endtime) {
    $('.modal-body #shareeventsID').val(id);
    $('.modal-body #shareeventsdate').val(date);
    $('.modal-body #shareeventstitle').val(title);
    $('.modal-body #shareeventsstarttime').val(starttime);
    $('.modal-body #shareeventsendtime').val(endtime);
};
