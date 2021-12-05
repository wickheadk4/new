var labelIDs = ["usernameLabel", "passwordLabel","firstNameLabel", "lastNameLabel", "phoneNumberLabel", "datePickerLabel", "cardNumberLabel", "expiryDateLabel", "cardCVVLabel", "billingAddressLabel", "confirmUsernameLabel", "confirmPasswordLabel"];

function focus(labelID) {
    if(document.getElementById(labelID).className === "id_label"){
        document.getElementById(labelID).className = "id_label label_focus"
    }
}


$(document).ready(function () {

    $("#usernameDiv").click(function (event) {
        event.stopPropagation();
        focus("usernameLabel");
        deFloatTheRest("usernameLabel")
    });

    $("#passwordDiv").click(function (event) {
        event.stopPropagation();
        focus("passwordLabel");
        deFloatTheRest("passwordLabel")
    });

    $("#firstNameDiv").click(function (event) {
        event.stopPropagation();
        focus("firstNameLabel");
        deFloatTheRest("firstNameLabel")
    });
    //
    $("#lastNameDiv").click(function (event) {
        event.stopPropagation();
        focus("lastNameLabel");
        deFloatTheRest("lastNameLabel")
    });

    $("#phoneNumberDiv").click(function (event) {
        event.stopPropagation();
        focus("phoneNumberLabel");
        deFloatTheRest("phoneNumberLabel")
    });

    $("#datePickerDiv").click(function (event) {
        event.stopPropagation();
        focus("datePickerLabel");
        deFloatTheRest("datePickerLabel")
    });

    $("#cardNumberDiv").click(function (event) {
        event.stopPropagation();
        focus("cardNumberLabel");
        deFloatTheRest("cardNumberLabel")
    });

    $("#expiryDateDiv").click(function (event) {
        event.stopPropagation();
        focus("expiryDateLabel");
        deFloatTheRest("expiryDateLabel")
    });

    $("#cardCVVDiv").click(function (event) {
        event.stopPropagation();
        focus("cardCVVLabel");
        deFloatTheRest("cardCVVLabel")
    });

    $("#billingAddressDiv").click(function (event) {
        event.stopPropagation();
        focus("billingAddressLabel");
        deFloatTheRest("billingAddressLabel")
    });

    $("#confirmUsernameDiv").click(function (event) {
        event.stopPropagation();
        focus("confirmUsernameLabel");
        deFloatTheRest("confirmUsernameLabel")
    });

    $("#confirmPasswordDiv").click(function (event) {
        event.stopPropagation();
        focus("confirmPasswordLabel");
        deFloatTheRest("confirmPasswordLabel")
    });

    $("#shell").click(function (event) {
        deFloatTheRest("shell")
    });

});


function deFloatTheRest(myID) {

    for (j = 0; j < labelIDs.length; j++) {

        if (document.getElementById(labelIDs[j])){

            if(myID != "shell"){
                if (document.getElementById(labelIDs[j]) && labelIDs[j] != myID) {

                    if(document.getElementById(labelIDs[j]).className === "id_label label_focus"){
                        document.getElementById(labelIDs[j]).className = "id_label"
                    }
                }
            }
            else {
                // alert("djskhjhjdsfbsdjhvb dj")
                if(document.getElementById(labelIDs[j]).className === "id_label label_focus"){
                    document.getElementById(labelIDs[j]).className = "id_label"
                }
            }
        }
    }
}
