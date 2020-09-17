Contact
#######
:date: 2019-10-18
:slug: contact
:status: published
:html_header:
   <script language="JavaScript" type="text/javascript">
   \  function decrypt_email(a) {
   \    // ROT13 : a Caesar cipher
   \    // letter -> letter' such that code(letter') = (code(letter) + 13) modulo 26
   \    return a.replace(/[a-zA-Z]/g,
   \                     function(c){
   \             return String.fromCharCode((c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26);
   \         })
   \  }
   \  // Generated using src/util.py
   \  function openPersonalMail(element) {
   \    var y = decrypt_email("znvygb:Nfujva Ivfuah Zbunana <nfujvaivf@cz.zr>");
   \    element.setAttribute("href", y);
   \  }
   \  function openWorkMail(element) {
   \    var y = decrypt_email("znvygb:Nfujva Ivfuah Zbunana <nizb@zvfh.fh.fr>");
   \    element.setAttribute("href", y);
   \  }
   \ </script>

I would love to hear from you!
Drop me a message if you wish to collaborate, or even leave a comment about my
research_ or software_ that I maintain.

.. raw:: html

   <table class="m-table m-flat m-big">
   <tbody>
     <tr>
       <td class="m-text-center">
         <div class="m-button m-info m-fullwidth" align-content="normal">
                   <div class="m-big"><b>Visiting address</b></div>
                   <span class="m-text m-small">
                       Arrhenius Laboratory, 6th Floor<br/>
                       Svante Arrhenius Väg 16C<br/>
                       Frescati Campus
                       Stockholm
                   </span>
         </div>
       </td>

       <td>
         <div class="m-button m-info m-fullwidth" align-content="normal">
                   <div class="m-big"><b>Mailing address</b></div>
                   <span class="m-text m-small">
                       Department of Meteorology<br/>
                       Stockholm University</br>
                       106 91 Stockholm
                       Sweden
                   </span>
         </div>
       </td>

     </tr>

     <tr>
     <td>
       <div class="m-button m-flat m-fullwidth">
         <a href="encrypted-personal-mail:Click to reveal" onclick="openPersonalMail(this);">
             <div class="m-big">Personal e-mail</div>
             <div class="m-small">Click to mail</div>
         </a>
       </div>
     </td>
     <td>
       <div class="m-button m-flat m-fullwidth">
         <a href="encrypted-work-mail:Click to reveal" onclick="openWorkMail(this);">
             <div class="m-big">Work e-mail</div>
             <div class="m-small">Click to mail</div>
         </a>
       </div>
     </td>
     </tr>

     </tbody>
     </table>

.. block-info:: Find directions to my office

    I try to be at the university once a week, despite working from home most
    of the time. Let me know beforehand if you drop by.

    .. container:: m-row

        .. container:: m-col-l-10 m-push-l-1 m-col-m-7 m-nopadb

            .. raw:: html

                <a href="https://www.qwant.com/maps/place/osm:way:63082892@Stockholm_University#map=11.00/59.3661410/18.0589277">
                <picture width="100%">
                  <source srcset="/images/contact_map.webp" type="image/webp"
                    width="100%">
                  <source srcset="/images/contact_map.jpg" type="image/jpeg"
                    width="100%">
                  <img src="/images/contact_map.jpg" width="100%">
                </picture>
                </a>



You can also reach me via social media accounts listed in the footer.

.. _research: /pages/research
.. _software: /pages/software

