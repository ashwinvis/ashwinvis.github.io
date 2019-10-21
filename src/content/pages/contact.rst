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
   \  function openMailer(element) {
   \    var y = decrypt_email("ashwinvis@protonmail.com");
   \    element.setAttribute("href", y);
   \  }
   </script>


Drop me a message if you wish to collaborate, or even leave a comment about my
research_ or software_ that I maintain. It

.. raw:: html

   <table class="m-table m-flat m-big">
   <tbody>
     <tr>
       <td class="m-text-center">
                   <div class="m-big">Visiting address</div>
                   <span class="m-text m-small m-dim">
                       Arrhenius Laboratory, 6th Floor<br/>
                       Svante Arrhenius Väg 16C<br/>
                       Frescati Campus
                       Stockholm
                   </span>
       </td>

       <td>
         <div class="m-button m-info m-fullwidth" align-content="normal">
                   <div class="m-big">Mailing address</div>
                   <span class="m-text m-small m-dim">
                       Department of Meteorology<br/>
                       Stockholm University</br>
                       106 91 Stockholm
                       Sweden
                   </span>
         </div>
       </td>

       <td>


.. image:: /images/contact_map.png
   :width: 10em
   :target: https://www.qwant.com/maps/place/osm:way:63082892@Stockholm_University#map=11.00/59.3661410/18.0589277
   :alt: Find directions to my office

.. raw:: html

       </td>

     </tr>
   </tbody>
   </table>

   <div class="m-button m-success m-fullwidth">
     <a href="encrypted-mail:Click to reveal" onclick="openMailer(this);">
         <div class="m-big">e-mail</div>
         <div class="m-small">Click to mail</div>
     </a>
   </div>



Social
------


.. _research: /pages/research
.. _software: /pages/software

