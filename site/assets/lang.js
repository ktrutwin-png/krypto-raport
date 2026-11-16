/* EN / PL switch for erl.grey83 pages.
   Static text: any element with data-pl="<Polish HTML>" (English stays in the markup).
   Dynamic text: listen for the "langchange" event and read window.LANG ("en" | "pl"). */
(function(){
 var K='erl_lang',L=null,T0=document.title;
 try{L=localStorage.getItem(K)}catch(e){}
 if(L!=='pl'&&L!=='en')L=(navigator.language||'').toLowerCase().indexOf('pl')===0?'pl':'en';
 window.LANG=L;
 function apply(){
  var h=document.documentElement;h.lang=L;
  document.querySelectorAll('[data-pl]').forEach(function(e){
   if(!e.hasAttribute('data-en'))e.setAttribute('data-en',e.innerHTML);
   e.innerHTML=L==='pl'?e.getAttribute('data-pl'):e.getAttribute('data-en')});
  document.title=L==='pl'&&h.dataset.titlePl?h.dataset.titlePl:T0;
  document.querySelectorAll('.lang [data-l]').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-l')===L?'true':'false')});
  try{document.dispatchEvent(new CustomEvent('langchange',{detail:L}))}catch(e){}
 }
 window.setLang=function(l){if(l!=='pl'&&l!=='en')return;L=window.LANG=l;try{localStorage.setItem(K,l)}catch(e){}apply()};
 document.addEventListener('click',function(ev){var b=ev.target.closest&&ev.target.closest('.lang [data-l]');if(b){ev.preventDefault();window.setLang(b.getAttribute('data-l'))}});
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',apply);else apply();
})();
