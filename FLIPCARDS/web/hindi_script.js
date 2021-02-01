$("document").ready(function (){

    var deck = new Array();
    var cdeck = new Array();
    var currcard = null;

    async function run(currcard) {    
        let n = await eel.say_words(currcard)();
        console.log("Got this from Python: " + n);
        return n
      }
    

      
  async function send_words(cdeck){
    console.log(cdeck);
    let n  = await eel.save_words(cdeck)();
    console.log("Got this from Python: " + n);
   }


   deck1 = eel.get_words()().then(
    function success(response) {
      console.log(response)
      Init(response);
    });


    function Init(response) {

        decklocal = JSON.parse(response);    
    
        for (var i = 0; i < decklocal.length; i++) {
          //  console.log(decklocal[i]);
          var card = {
            card: 1 + i,
            question: decklocal[i][0],
            answer: decklocal[i][1], //"टायपिंग"
            num: decklocal[i][2],
            active: decklocal[i][3]
          };
    
          
          deck.push(card);
    
          //  console.log(card.picture, card.sound);      
          //   $('#store').prepend("<img id=" + card.card + " src=" + card.picture + " style='width:300px;height:300px;'/>");
        };
    
        console.log(deck.length);
        Draw();
      };
    

      
  function Draw() {


    if (deck.length == 0) {
      ClearText();
      send_words(cdeck);
    }

    if (deck !== null) {


      currcard = deck.shift();
      if (currcard !== null) {
        console.log(currcard);
        $("#hindi").text (currcard.answer);
        $("#headlight").text (currcard.question);
        run(currcard)

      }

      $("#msg").text(deck.length +1 +" Cards left");

    }

  }

  function ClearText() {
    $("#msg").text("Good Job !!");
    $("#fc").fadeOut(2000);
    // startConfetti();
    confetti.start();
  };


  $('#yes').click(function () {

    if (currcard.num < 11) {
      currcard.num = currcard.num + 1;
    }
    if (currcard.num > 11) {
      currcard.num = 11;
    }
    cdeck.push(currcard);
    Draw();

  });

  $('#no').click(function () {

    if (currcard.num >= 1) {
      currcard.num = currcard.num - 1;
    }

    deck.push(currcard);
    Draw();

  });

  $('#play').click(function () {
    if (currcard !== null) {
    run(currcard);
    }
  });


})