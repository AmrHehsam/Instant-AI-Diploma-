(function(g){var window=this;'use strict';var Emb=function(a,b){g.W.call(this,{I:"button",Na:["ytp-miniplayer-expand-watch-page-button","ytp-button","ytp-miniplayer-button-top-left"],Y:{title:"{{title}}","data-tooltip-target-id":"ytp-miniplayer-expand-watch-page-button","aria-keyshortcuts":"i","data-title-no-tooltip":"{{data-title-no-tooltip}}"},X:[{I:"svg",Y:{height:"24px",version:"1.1",viewBox:"0 0 24 24",width:"24px"},X:[{I:"g",Y:{fill:"none","fill-rule":"evenodd",stroke:"none","stroke-width":"1"},X:[{I:"g",Y:{transform:"translate(12.000000, 12.000000) scale(-1, 1) translate(-12.000000, -12.000000) "},
X:[{I:"path",Y:{d:"M19,19 L5,19 L5,5 L12,5 L12,3 L5,3 C3.89,3 3,3.9 3,5 L3,19 C3,20.1 3.89,21 5,21 L19,21 C20.1,21 21,20.1 21,19 L21,12 L19,12 L19,19 Z M14,3 L14,5 L17.59,5 L7.76,14.83 L9.17,16.24 L19,6.41 L19,10 L21,10 L21,3 L14,3 Z",fill:"#fff","fill-rule":"nonzero"}}]}]}]}]});this.J=a;this.Ta("click",this.onClick,this);this.updateValue("title",g.LQ(a,"Expand","i"));this.update({"data-title-no-tooltip":"Expand"});g.qb(this,g.EQ(b.Ec(),this.element))},Fmb=function(a){g.W.call(this,{I:"div",
T:"ytp-miniplayer-ui"});this.xg=!1;this.player=a;this.V(a,"minimized",this.Fh);this.V(a,"onStateChange",this.XQ)},Gmb=function(a){g.CR.call(this,a);
this.B=new g.KL(this);this.j=new Fmb(this.player);this.j.hide();g.jQ(this.player,this.j.element,4);a.yg()&&(this.load(),g.mr(a.getRootNode(),"ytp-player-minimized",!0))};
g.x(Emb,g.W);Emb.prototype.onClick=function(){this.J.Ua("onExpandMiniplayer")};g.x(Fmb,g.W);g.k=Fmb.prototype;
g.k.NN=function(){this.tooltip=new g.dU(this.player,this);g.H(this,this.tooltip);g.jQ(this.player,this.tooltip.element,4);this.tooltip.scale=.6;this.bd=new g.jS(this.player);g.H(this,this.bd);this.rk=new g.W({I:"div",T:"ytp-miniplayer-scrim"});g.H(this,this.rk);this.rk.Ga(this.element);this.V(this.rk.element,"click",this.II);var a=new g.W({I:"button",Na:["ytp-miniplayer-close-button","ytp-button"],Y:{"aria-label":"Close"},X:[g.AG()]});g.H(this,a);a.Ga(this.rk.element);this.V(a.element,"click",this.Fp);
a=new Emb(this.player,this);g.H(this,a);a.Ga(this.rk.element);this.ov=new g.W({I:"div",T:"ytp-miniplayer-controls"});g.H(this,this.ov);this.ov.Ga(this.rk.element);this.V(this.ov.element,"click",this.II);var b=new g.W({I:"div",T:"ytp-miniplayer-button-container"});g.H(this,b);b.Ga(this.ov.element);a=new g.W({I:"div",T:"ytp-miniplayer-play-button-container"});g.H(this,a);a.Ga(this.ov.element);var c=new g.W({I:"div",T:"ytp-miniplayer-button-container"});g.H(this,c);c.Ga(this.ov.element);this.DY=new g.pT(this.player,
this,!1);g.H(this,this.DY);this.DY.Ga(b.element);b=new g.oT(this.player,this);g.H(this,b);b.Ga(a.element);this.nextButton=new g.pT(this.player,this,!0);g.H(this,this.nextButton);this.nextButton.Ga(c.element);this.Gj=new g.WT(this.player,this);g.H(this,this.Gj);this.Gj.Ga(this.rk.element);this.Sc=new g.uT(this.player,this);g.H(this,this.Sc);g.jQ(this.player,this.Sc.element,4);this.qI=new g.W({I:"div",T:"ytp-miniplayer-buttons"});g.H(this,this.qI);g.jQ(this.player,this.qI.element,4);a=new g.W({I:"button",
Na:["ytp-miniplayer-close-button","ytp-button"],Y:{"aria-label":"Close"},X:[g.AG()]});g.H(this,a);a.Ga(this.qI.element);this.V(a.element,"click",this.Fp);a=new g.W({I:"button",Na:["ytp-miniplayer-replay-button","ytp-button"],Y:{"aria-label":"Close"},X:[g.lsa()]});g.H(this,a);a.Ga(this.qI.element);this.V(a.element,"click",this.q8);this.V(this.player,"presentingplayerstatechange",this.Xd);this.V(this.player,"appresize",this.Mb);this.V(this.player,"fullscreentoggled",this.Mb);this.Mb()};
g.k.show=function(){this.Bf=new g.Zq(this.qw,null,this);this.Bf.start();this.xg||(this.NN(),this.xg=!0);0!==this.player.getPlayerState()&&g.W.prototype.show.call(this);this.Sc.show();this.player.unloadModule("annotations_module")};
g.k.hide=function(){this.Bf&&(this.Bf.dispose(),this.Bf=void 0);g.W.prototype.hide.call(this);this.player.yg()||(this.xg&&this.Sc.hide(),this.player.loadModule("annotations_module"))};
g.k.ya=function(){this.Bf&&(this.Bf.dispose(),this.Bf=void 0);g.W.prototype.ya.call(this)};
g.k.Fp=function(){this.player.stopVideo();this.player.Ua("onCloseMiniplayer")};
g.k.q8=function(){this.player.playVideo()};
g.k.II=function(a){if(a.target===this.rk.element||a.target===this.ov.element)g.dS(this.player.Tb())?this.player.pauseVideo():this.player.playVideo()};
g.k.Fh=function(){g.mr(this.player.getRootNode(),"ytp-player-minimized",this.player.yg())};
g.k.bf=function(){this.Sc.Hc();this.Gj.Hc()};
g.k.qw=function(){this.bf();this.Bf&&this.Bf.start()};
g.k.Xd=function(a){g.aH(a.state,32)&&this.tooltip.hide()};
g.k.Mb=function(){g.GT(this.Sc,0,this.player.qb().getPlayerSize().width,!1);g.vT(this.Sc)};
g.k.XQ=function(a){this.player.yg()&&(0===a?this.hide():this.show())};
g.k.Ec=function(){return this.tooltip};
g.k.Mg=function(){return!1};
g.k.Ng=function(){return!1};
g.k.wm=function(){return!1};
g.k.HJ=function(){};
g.k.lq=function(){};
g.k.Wy=function(){};
g.k.hn=function(){return null};
g.k.eH=function(){return null};
g.k.fN=function(){return new g.ue(0,0)};
g.k.Ok=function(){return new g.vo(0,0,0,0)};
g.k.handleGlobalKeyDown=function(){return!1};
g.k.handleGlobalKeyUp=function(){return!1};
g.k.Ew=function(a,b,c,d,e){var f=0,h=d=0,l=g.Jo(a);if(b){c=g.hr(b,"ytp-prev-button")||g.hr(b,"ytp-next-button");var m=g.hr(b,"ytp-play-button"),n=g.hr(b,"ytp-miniplayer-expand-watch-page-button");c?f=h=12:m?(b=g.Ho(b,this.element),h=b.x,f=b.y-12):n&&(h=g.hr(b,"ytp-miniplayer-button-top-left"),f=g.Ho(b,this.element),b=g.Jo(b),h?(h=8,f=f.y+40):(h=f.x-l.width+b.width,f=f.y-20))}else h=c-l.width/2,d=25+(e||0);b=this.player.qb().getPlayerSize().width;e=f+(e||0);l=g.pe(h,0,b-l.width);e?(a.style.top=e+"px",
a.style.bottom=""):(a.style.top="",a.style.bottom=d+"px");a.style.left=l+"px"};
g.k.showControls=function(){};
g.k.Up=function(){};
g.k.mm=function(){return!1};
g.k.cF=function(){};
g.k.WA=function(){};
g.k.Gr=function(){};
g.k.Fr=function(){};
g.k.uy=function(){};
g.k.Ps=function(){};
g.k.NE=function(){};g.x(Gmb,g.CR);g.k=Gmb.prototype;g.k.onVideoDataChange=function(){if(this.player.getVideoData()){var a=this.player.getVideoAspectRatio(),b=16/9;a=a>b+.1||a<b-.1;g.mr(this.player.getRootNode(),"ytp-rounded-miniplayer-not-regular-wide-video",a)}};
g.k.create=function(){g.CR.prototype.create.call(this);this.B.V(this.player,"videodatachange",this.onVideoDataChange);this.onVideoDataChange()};
g.k.wl=function(){return!1};
g.k.load=function(){this.player.hideControls();this.j.show()};
g.k.unload=function(){this.player.showControls();this.j.hide()};g.BR("miniplayer",Gmb);})(_yt_player);
