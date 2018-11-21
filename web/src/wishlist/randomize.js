var nodemailer = require('nodemailer');
//var santa = require('/creds')
function randomize (peopleKeys, peopleObj) {
    //will randomize the keys of people and use that as the index to select
    //people are the keys in string
    var randomOrder = [];
    const size = peopleKeys.length;
    peopleKeys.forEach(function (personKey){
        randomOrder.splice(randomNum(size), 0, personKey);
    });

    //now with a random order we can start sending emails
    randomOrder.forEach(function( person, index ){
        //will use index +1 and +2 to get the next person's info
        //check if the index is out of bounds
        var firstIndex = (index + 1) % size; //will give to this person
        //also means you and the person of index -1 will be helping this person
        var firstHelperIndex = (index -1 + size) % size;
        var secondIndex = (index + 2) % size; //will give to this person with person index 1 
        var name1 = randomOrder[firstIndex];
        var person1 = peopleObj[name1];
        var text1 = xmasMessage(person1.fullName, )
    })
}

function randomNum( size ){
    return Math.floor(Math.random() * size);
}

const santa = {
    email: '',
    pass: 'test'
}

function sendMail( receiver, text){
    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: santa.email,
            pass: santa.pass
        }
    });

    var mailOptions = {
        from: santa.email,
        to: receiver,
        subject: 'Santa!',
        text: text
    };

    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }   
    });
};

function xmasMessage( receiver, secondSanta){
    return 'Tu le daras regalo a '+ receiver + ' con la ayuda de ' +secondSanta;
}