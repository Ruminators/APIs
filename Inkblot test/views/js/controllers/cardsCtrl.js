
//const remote=require('electron').remote;

app.controller('cardsCtrl',function($rootScope, $document,$scope,$timeout,$http,$mdColors,$mdDialog,$timeout, $q, $log, Animations,hotkeys) {
    var self = this;
  self.refresh=()=>{
    location.reload(true)
  }
  self.processchk=()=>{
    return self.process
  }
   self.process=false
    evaluate=(ans)=>{
      var config = {
          method: "POST",
          url: '../api/ans',
          data: ans,
          headers: {
              'Content-Type': 'application/json; charset=utf-8'
          }
      };
      console.log('/api/ans')
      return $http(config);
  }

  self.testchk=true

self.keys=()=>{
  return Object.keys(self.selected).length
}

  self.done=()=>{
    console.log(self.selected)
    self.process=true
    evaluate(self.selected).then((res)=>{

      self.testchk=false
      self.test=res.data
      self.process=false
      self.final=true
    })
  }
  self.final=false
  self.reset=()=>{
    self.selected=null
    self.selected={}
  }
  self.checkd=()=>{
    if(Object.keys(self.selected).length>=9 && !self.processchk())
      return false
      else return true
  }
    self.selected={}
    console.log(self.selected)
    self.cards=[{"content": ["I see a face in the card", "I see a scary face in the card", "Things look like they're whirling around in the card", "It looks like we're looking down on people or something in the card", "I see a mask in the card", "I see a flower in the card", "I see some sexual imagery in the card" ], "step": 0, "ink": "http://theinkblot.com/image/plate1.gif"}, {"content": ["It looks like a bunny rabbit head", "It looks like an elongated horse's head", "It looks like an X-ray, especially that part near the bottom", "It looks like spilled ink that was blotted", "It looks like two distorted Eskimos playing \"patty-cake\"", "It looks like a giant open mouth, about to devour me", "It looks like a tunnel into another dimension, or maybe New Jersey" ], "step": 1, "ink": "http://theinkblot.com/image/plate2.gif"}, {"content": ["It looks like two double-amputees dancing", "It looks like the coast of Italy after an atom bomb attack, only mirrored", "It looks like a pair of one-legged cannibals fighting over a victim", "I love pudding", "It looks like an RLFP DNA test result, with the phenotypes split", "It looks like Satan's head, the white part in the middle (can't you see it?)", "It looks like smudges, or maybe an inkblot" ], "step": 2, "ink": "http://theinkblot.com/image/plate3.gif"}, {"content": ["It looks like the Universe exploding and coming at me", "No, you idiot, it's a butterfly that's been crushed by a bootheel", "Ha! This one is definitely an inkblot", "The dark, malevolent shapes remind me of my childhood murder-spree", "I see someone standing on someone else's head with their hands out", "It looks like something under a microscope slide or something", "It looks like someone exposing herself to me, heh heh!" ], "step": 3, "ink": "http://theinkblot.com/image/plate4.gif"}, {"content": ["I see Satan's eyes, filled with an evil, burning hatred for my soul", "I see a fluffy bunny-rabbit", "I see a big naughty shape at the top, in the center", "It looks like a guy that was hit by a bullet-train going 5 million miles an hour", "This blot doesn't really look like anything to me. Can we have some lunch?", "It looks like a Tele-Tubby (maybe 'Po'?) that was run over by a Sherman Tank", "It looks like you just threw ink on a paper and then folded it" ], "step": 4, "ink": "http://theinkblot.com/image/plate5.gif"}, {"content": ["This card gives me strong yearnings for members of my sex", "I see a monster swooping down to eat a helpless puppy dog", "It looks like people having sex, seen from below, not that I'd know...", "It looks like you folded the card top-to-bottom this time", "It looks like a pulsing heart, ripped from the chest of its victim. (No, really.)", "It looks like something a brain-damaged kid would draw in Art Class", "It looks like a lawyer with his arms out, demanding money" ], "step": 5, "ink": "http://theinkblot.com/image/plate6.gif"}, {"content": ["It looks like a bat, no wait, a dog, no, I mean a cat, oh, hell, I give up!!", "It looks like two evil garden gnomes, conspiring with each other.", "It looks like, well, something, you know, kinda blobby and all", "It looks like a giraffe in a bathtub filled with brightly-colored machine tools", "It looks like conflict between my id and my repressed superego. Or something.", "It looks like a fractal image that some bozo whipped up in PhotoShop\u00ae", "Heck, I'm drawing a blank on this one. Can I get a hint?" ], "step": 6, "ink": "http://theinkblot.com/image/plate7.gif"}, {"content": ["It looks like a leaf. Or animals climbing up a cave wall.", "It looks like something verrrrrrry sexy. Heheh, heheh!", "I think this is the same as card #4. Or maybe #5.", "It looks like a Rigelian Brain Eater from Star Trek.", "It looks like that guy on American Idol. You know which one I mean.", "It looks like a chest X-ray. Yeah, that's it. A chest X-ray.", "It looks like death reaching out for my mortal soul." ], "step": 7, "ink": "http://theinkblot.com/image/plate8.gif"}, {"content": ["It looks like a monster. Hold me, I'm scared!", "I see naughty bits! lol, lol!", "It looks like an abstract pattern of light and dark things.", "I don't know, but I wouldn't want to meet it in a dark alley.", "It looks kinda like my ex-wife, first thing in the morning.", "I must kill them all, kill them and then ...ummm, what were you saying?", "It looks like toad that tried to cross the highway. At rush hour." ], "step": 8, "ink": "http://theinkblot.com/image/plate9.gif"}, {"content": ["This is a bad acid trip I had at a Styx concert.", "This is a copyrighted image and my lawyer will be in touch.", "It looks like Indian shamans, dancing around a fire.", "It looks like something really indescribable.", "It looks like a decaying soul, ravaged by life's many horrors. Or a doggy.", "This is the Devil for sure. You can't fool me, Spawn Of Satan!", "This looks an awful lot like the stain on my pillow."], "step": 9, "ink": "http://theinkblot.com/image/plate10.gif"}]    

    {}
    self.colors=$mdColors;
    self.cardAnim = Animations;
    self.clickClose=function(){
        remote.app.quit();
    }
    self.minimize=function(){
      remote.getCurrentWindow().minimize();
    }
    self.toggleFullscreen=function(){
      
      
      if(!self.iconFullscreen)
      {remote.getCurrentWindow().setFullScreen(true);
        self.iconFullscreen='_exit'}
      else
      {remote.getCurrentWindow().setFullScreen(false);
        self.iconFullscreen='';}
    }
    

    // ******************************
    // Internal methods
    // ******************************

    /**
     * Search for states... use $timeout to simulate
     * remote dataservice call.
     */
    






    /******************************* handling dialog popup events *******************************************/

    /*
   $mdDialog.show({
          templateUrl:'dialogs/deletePatient.html',
          clickOutsideToClose:false,
          hasBackdrop:true,
          targetEvent:ev,
          fullscreen:false,
          controller:'addPatientCtrl',
          
        })*/

    

});

