@font-face {
  font-family: "Karla-Regular";
  font-display: swap;
  src: url("../../fonts/Karla/Karla-Regular.ttf") format("truetype"); }
@font-face {
  font-family: "Karla-Bold";
  font-display: swap;
  src: url("../../fonts/Karla/Karla-Bold.ttf") format("truetype"); }
@font-face {
  font-family: "Karla-BoldItalic";
  font-display: swap;
  src: url("../../fonts/Karla/Karla-BoldItalic.ttf") format("truetype"); }
@font-face {
  font-family: "Karla-Italic";
  font-display: swap;
  src: url("../../fonts/Karla/Karla-Italic.ttf") format("truetype"); }
@font-face {
  font-family: "PlayfairDisplay-Regular";
  font-display: swap;
  src: url("../../fonts/Playfair_Display/PlayfairDisplay-Regular.ttf") format("truetype"); }
@font-face {
  font-family: "PlayfairDisplay-Black";
  font-display: swap;
  src: url("../../fonts/Playfair_Display/PlayfairDisplay-Black.ttf") format("truetype"); }
@font-face {
  font-family: "PlayfairDisplay-Bold";
  font-display: swap;
  src: url("../../fonts/Playfair_Display/PlayfairDisplay-Bold.ttf") format("truetype"); }
@font-face {
  font-family: "PlayfairDisplay-Italic";
  font-display: swap;
  src: url("../../fonts/Playfair_Display/PlayfairDisplay-Italic.ttf") format("truetype"); }
@font-face {
  font-family: "PlayfairDisplay-BoldItalic";
  font-display: swap;
  src: url("../../fonts/Playfair_Display/PlayfairDisplay-BoldItalic.ttf") format("truetype"); }
@font-face {
  font-family: "Montserrat-Light";
  font-display: swap;
  src: url("../../fonts/Montserrat/Montserrat-Light.ttf") format("truetype"); }
@font-face {
  font-family: "Montserrat-Regular";
  font-display: swap;
  src: url("../../fonts/Montserrat/Montserrat-Regular.ttf") format("truetype"); }
@font-face {
  font-family: "Montserrat-SemiBold";
  font-display: swap;
  src: url("../../fonts/Montserrat/Montserrat-SemiBold.ttf") format("truetype"); }
@font-face {
  font-family: "Montserrat-Bold";
  font-display: swap;
  src: url("../../fonts/Montserrat/Montserrat-Bold.ttf") format("truetype"); }
body {
  background-color: #f5f5f5;
  padding-bottom: 5rem; }

a {
  color: black; }
  a:hover, a:active, a:focus {
    color: black;
    text-decoration: none;
    text-transform: none; }

.image-wrapper {
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
  align-content: center; }
  .image-wrapper img {
    width: 70%;
    margin-left: 30%; }

.page-title {
  font-family: Karla-Bold;
  font-size: 32px; }

.content-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  align-content: center;
  height: 100vh; }

.label-input p {
  font-family: Karla-Regular;
  font-size: 14px; }
.label-input input {
  font-family: Karla-Regular;
  letter-spacing: 1.3px;
  width: 100%;
  border: none;
  border-bottom: solid 1px lightgrey;
  height: 45px;
  font-size: 16px;
  padding: 10px 10px;
  transition: all 0.2s ease-in-out; }
  .label-input input:focus {
    border: none !important;
    border-bottom: solid 1px #6c61f6 !important;
    box-shadow: unset;
    outline: none; }
.label-input ::placeholder {
  color: grey;
  font-size: 14px;
  font-family: Karla-Regular; }
.label-input .field-wrapper {
  margin-bottom: 20px; }
.label-input .form-submit-btn {
  margin-top: 30px;
  font-family: Karla-Bold;
  font-size: 16px;
  display: block;
  width: 100%;
  height: 60px;
  background: #333;
  color: white;
  border: none; }
  .label-input .form-submit-btn:focus {
    border: none !important;
    border-bottom: none !important; }
.label-input .form-link {
  margin-top: 10px;
  display: block;
  text-align: center;
  font-family: Karla-Regular;
  font-size: 16px;
  color: #6c61f6;
  width: 100%; }
  .label-input .form-link:hover {
    text-decoration: none;
    text-transform: none; }

.books-feed-section .search-results {
  display: block !important; }

i {
  border: solid black;
  border-width: 0 3px 3px 0;
  display: inline-block;
  padding: 3px; }

.right {
  transform: rotate(-45deg);
  -webkit-transform: rotate(-45deg); }

.left {
  transform: rotate(135deg);
  -webkit-transform: rotate(135deg); }

nav {
  padding: 1rem 0;
  background-color: #6c61f6;
  background-color: transparent;
  position: absolute;
  top: 0;
  margin-left: 50%;
  transform: translateX(-50%);
  margin-top: 1.5rem;
  z-index: 9999; }
  nav.color-nav {
    background-color: #6c61f6;
    padding: 1rem 0;
    background-color: #6c61f6;
    width: 100vw;
    position: relative;
    margin-top: 0;
    z-index: 9999; }
  nav .brand,
  nav .search,
  nav .action-links {
    display: inline-block; }
    nav .brand:focus,
    nav .search:focus,
    nav .action-links:focus {
      text-transform: none;
      text-decoration: none; }
  nav .brand {
    line-height: 4rem;}
    nav .brand a {
      color: white;
      font-family: PlayfairDisplay-Black;
      font-size: 3.2rem; }
      nav .brand a:hover {
        text-decoration: none;
        text-transform: none; }
  nav .search {
    display: none;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    margin: 0;
    padding: 0; }
    nav .search form {
      margin: 0; }
      nav .search form input {
        width: 70rem;
        height: 4rem;
        padding: 1rem;
        font-family: Karla-Regular;
        border: solid 1px #6c61f6;
        border-radius: 2px;
        outline: none;
        box-sizing: border-box; }
        nav .search form input:focus {
          width: 70rem;
          height: 4rem;
          border: solid 1px black;
          padding: 1rem; }
      nav .search form button {
        padding: 1rem; }
  nav .action-links {
    line-height: 4rem;
    list-style-type: none;
    padding: 0;
    margin: 0; }
    nav .action-links li {
      display: inline-block; }
      nav .action-links li a {
        color: white;
        font-family: Karla-Bold; }
        nav .action-links li a:hover {
          text-decoration: none;
          text-transform: none; }
      nav .action-links li .sell-btn {
        margin-right: 2rem;
        padding: 1rem 3rem;
        background-color: white;
        color: #6c61f6;
        color: #000;
        border-radius: 32px; }

.forgot-pass-section {
  background-color: white; }
  .forgot-pass-section .image-wrapper {
    display: flex;
    height: 100vh;
    justify-content: center;
    align-items: center;
    align-content: center; }
    .forgot-pass-section .image-wrapper img {
      width: 70%; }
  .forgot-pass-section .content-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    align-content: center;
    height: 100vh; }
    .forgot-pass-section .content-wrapper h2 {
      font-family: PlayfairDisplay-Bold;
      font-size: 50px;
      width: 49%;
      margin-bottom: 50px; }
    .forgot-pass-section .content-wrapper form {
      width: 50%; }
      .forgot-pass-section .content-wrapper form input {
        font-family: Karla-Regular;
        letter-spacing: 1.3px;
        width: 100%;
        border: none;
        border-bottom: solid 1px lightgrey;
        font-size: 16px;
        padding: 10px 15px;
        transition: all 0.2s ease-in-out; }
        .forgot-pass-section .content-wrapper form input:focus {
          border: none !important;
          border-bottom: solid 1px #6c61f6 !important;
          box-shadow: unset;
          outline: none; }
      .forgot-pass-section .content-wrapper form ::placeholder {
        color: grey;
        font-size: 14px;
        font-family: Karla-Regular; }
      .forgot-pass-section .content-wrapper form .reset-pass-btn {
        margin-top: 30px;
        font-family: Karla-Bold;
        font-size: 16px;
        display: block;
        width: 100%;
        padding: 1.5rem;
        background: #333;
        color: white;
        border-bottom: none;
        border-radius: 4px;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.2); }
        .forgot-pass-section .content-wrapper form .reset-pass-btn:hover {
          box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.12); }
        .forgot-pass-section .content-wrapper form .reset-pass-btn:focus {
          border: none !important;
          border-bottom: none !important; }
      .forgot-pass-section .content-wrapper form .login-page-btn {
        margin-top: 10px;
        display: block;
        text-align: center;
        font-family: Karla-Regular;
        font-size: 16px;
        color: #6c61f6;
        width: 100%; }

.title {
  font-family: Karla-Bold;
  font-size: 3.5rem;
  margin: 0;
  margin-bottom: 2rem; }

.featured-books {
  background-color: #eef2f5; }
  .featured-books .title {
    font-size: 3.5rem; }

.all-books {
  display: flex;
  padding: 8rem 0 10rem 0; }
  .all-books h1 {
    font-size: 2.5rem; }
  .all-books .book-card-wrapper {
    background-color: white;
    border-radius: 4px;
    border: solid 0.5px lightgrey;
    margin-bottom: 2.5rem; }
    .all-books .book-card-wrapper:hover {
      box-shadow: 0 1px 2px 0 rgba(60, 64, 67, 0.302), 0 1px 3px 1px rgba(60, 64, 67, 0.149); }
    .all-books .book-card-wrapper a {
      font-family: Karla-Regular;
      color: #333333; }
      .all-books .book-card-wrapper a .book-card {
        display: flex;
        height: 20rem;
        padding: 2rem;
        align-items: center; }
        .all-books .book-card-wrapper a .book-card .col-A {
          flex: 1;
          text-align: center; }
          .all-books .book-card-wrapper a .book-card .col-A img {
            width: 8rem;
            height: 12rem;
            border-radius: 4px; }
        .all-books .book-card-wrapper a .book-card .col-B {
          flex: 2;
          margin-left: 1rem;
          height: 100%; }
          .all-books .book-card-wrapper a .book-card .col-B .b-name {
            font-family: Karla-Bold;
            text-transform: capitalize;
            font-size: 2rem; }
          .all-books .book-card-wrapper a .book-card .col-B .b-username {
            font-family: Montserrat-Regular;
            text-transform: capitalize;
            font-size: 1.6rem; }
            .all-books .book-card-wrapper a .book-card .col-B .b-username span {
              font-family: Montserrat-SemiBold;
              font-size: 1.2rem; }
          .all-books .book-card-wrapper a .book-card .col-B .b-price {
            font-family: Montserrat-Bold;
            font-size: 2.2rem; }
            .all-books .book-card-wrapper a .book-card .col-B .b-price span {
              font-family: Montserrat-SemiBold;
              font-size: 1.2rem; }
      .all-books .book-card-wrapper a:hover {
        text-transform: none;
        text-decoration: none; }

.view-book-detail-page {
  background: white; }
  .view-book-detail-page .book-section {
    background: white;
    padding: 10rem 0;
    font-family: Karla-Regular;
    letter-spacing: -0.5px;
    border-bottom: solid 1px #e5e5e5; }
    .view-book-detail-page .book-section .book-details-left {
      padding: 3rem; }
      .view-book-detail-page .book-section .book-details-left img {
        width: 19rem;
        height: 26rem;
        display: inline-block; }
    .view-book-detail-page .book-section .book-details-right {
      border-right: solid 1px #e5e5e5;
      padding-right: 2rem; }
      .view-book-detail-page .book-section .book-details-right h1 {
        font-family: PlayfairDisplay-Bold;
        font-size: 4rem;
        text-transform: capitalize; }
      .view-book-detail-page .book-section .book-details-right h6 {
        font-family: Karla-Regular;
        font-size: 1.8rem; }
      .view-book-detail-page .book-section .book-details-right p {
        font-family: Karla-Bold;
        font-size: 4rem; }
        .view-book-detail-page .book-section .book-details-right p span {
          font-family: Karla-Regular;
          font-size: 4rem; }
      .view-book-detail-page .book-section .book-details-right .hightlights-wrapper h5 {
        font-family: Karla-Bold;
        margin-bottom: 1.5rem; }
      .view-book-detail-page .book-section .book-details-right .hightlights-wrapper table {
        width: 100%; }
        .view-book-detail-page .book-section .book-details-right .hightlights-wrapper table td {
          padding-bottom: 1rem; }
    .view-book-detail-page .book-section .contact-details-wrapper {
      padding-top: 2rem;
      height: 35rem;
      position: relative; }
      .view-book-detail-page .book-section .contact-details-wrapper h3 {
        font-family: Karla-Bold;
        font-size: 3rem;
        margin-bottom: 2.5rem;
        margin-top: 0rem; }
      .view-book-detail-page .book-section .contact-details-wrapper .contact-wrapper p {
        font-size: 1.5rem;
        margin-bottom: 0; }
      .view-book-detail-page .book-section .contact-details-wrapper .contact-wrapper h6 {
        font-family: Karla-Bold;
        font-size: 2.4rem;
        margin-top: 0.5rem;
        margin-bottom: 2rem; }
      .view-book-detail-page .book-section .contact-details-wrapper .contact-wrapper a {
        font-family: Karla-Bold;
        display: inline-block;
        background-color: #6c61f6;
        color: white;
        padding: 1rem;
        border-radius: 4px;
        width: 100%;
        text-align: center;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.2); }
        .view-book-detail-page .book-section .contact-details-wrapper .contact-wrapper a:hover {
          box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.12); }
      .view-book-detail-page .book-section .contact-details-wrapper .note-wrapper {
        background-color: aliceblue;
        padding: 2rem;
        border-radius: 4px;
        margin-top: 0.5rem;
        position: absolute;
        bottom: 10; }
        .view-book-detail-page .book-section .contact-details-wrapper .note-wrapper h6 {
          font-family: Karla-Bold;
          font-size: 1.8rem;
          margin-top: 0; }
        .view-book-detail-page .book-section .contact-details-wrapper .note-wrapper p {
          font-family: Karla-Regular;
          margin-bottom: 1rem; }
          .view-book-detail-page .book-section .contact-details-wrapper .note-wrapper p:last-child {
            margin-bottom: 0; }
  .view-book-detail-page .top-books-section {
    margin-top: 0; }
    .view-book-detail-page .top-books-section .section-title {
      text-align: center; }
    .view-book-detail-page .top-books-section .books-wrapper {
      padding: 4rem !important; }

.section-title {
  font-family: PlayfairDisplay-Bold;
  font-size: 3rem;
  margin: 0;
  background: white;
  border-top-left-radius: 6px;
  border-top-right-radius: 6px;
  padding: 5rem 0 0 4rem; }
  .section-title span img {
    width: 2rem;
    margin-right: 2rem;
    vertical-align: inherit; }

.above-fold-section {
  position: relative;
  background-image: url("../../image/ab-2.jpg");
  height: 100vh;
  background-size: cover; }
  .above-fold-section .black-overlay {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: black;
    opacity: 0.7; }
  .above-fold-section .content {
    position: relative;
    text-align: center;
    padding-top: 35rem; }
    .above-fold-section .content h1 {
      font-family: PlayfairDisplay-Black;
      font-size: 4rem;
      color: white;
      letter-spacing: 1.5px; }
    .above-fold-section .content .title-wrapper {
      color: white;
      margin-top: 12rem; }
      .above-fold-section .content .title-wrapper h2 {
        font-family: Karla-Regular;
        letter-spacing: -0.5px;
        font-size: 2rem; }
        .above-fold-section .content .title-wrapper h2 span {
          font-family: Karla-Regular; }
    .above-fold-section .content .search-wrapper input {
      font-family: Karla-Regular;
      font-size: 1.6rem;
      color: black;
      width: 60rem;
      height: 5.5rem;
      padding: 1rem 2rem;
      border-radius: 34px;
      border: none; }
      .above-fold-section .content .search-wrapper input:focus {
        outline: none; }
    .above-fold-section .content .search-wrapper ::placeholder {
      color: grey; }

.top-books-section {
  position: relative;
  margin-top: -8rem; }
  .top-books-section .slider-wrapper {
    position: relative;
    background: white; }
    .top-books-section .slider-wrapper button {
      position: absolute;
      top: 45%;
      transform: translateY(-50%);
      z-index: 99;
      width: 5rem;
      height: 5rem;
      background: transparent;
      border: none; }
      .top-books-section .slider-wrapper button:focus {
        outline: none; }
    .top-books-section .slider-wrapper .right-arrow {
      right: 3rem; }
    .top-books-section .slider-wrapper .left-arrow {
      left: 3rem; }
    .top-books-section .slider-wrapper .inner-wrapper {
      padding: 0 4rem; }
      .top-books-section .slider-wrapper .inner-wrapper .books-wrapper {
        background: white;
        padding: 7rem 4rem;
        border-bottom-left-radius: 6px;
        border-bottom-right-radius: 6px;
        display: flex; }
        .top-books-section .slider-wrapper .inner-wrapper .books-wrapper .wrapper {
          text-align: center;
          flex: 1;
          margin: 0 1.5rem; }
          .top-books-section .slider-wrapper .inner-wrapper .books-wrapper .wrapper img {
            border-radius: 0.5rem;
            display: inline-block;
            width: 14rem;
            height: 20rem; }
          .top-books-section .slider-wrapper .inner-wrapper .books-wrapper .wrapper p {
            font-family: Karla-Regular;
            letter-spacing: -0.5px;
            font-size: 1.6rem;
            margin-top: 1rem;
            margin-bottom: 0; }

.top-categories-section {
  margin-top: 5rem; }
  .top-categories-section .categories-wrapper {
    padding: 7rem 4rem;
    background: white;
    display: flex; }
    .top-categories-section .categories-wrapper .category {
      flex: 1;
      margin: 0 2rem;
      display: flex;
      padding: 2rem;
      justify-content: center;
      border-radius: 6px; }
      .top-categories-section .categories-wrapper .category:hover {
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.2); }
      .top-categories-section .categories-wrapper .category:first-child {
        margin-left: 0; }
      .top-categories-section .categories-wrapper .category:last-child {
        margin-right: 0; }
      .top-categories-section .categories-wrapper .category img {
        width: 4.5rem;
        height: 8rem; }
      .top-categories-section .categories-wrapper .category p {
        font-family: Karla-Regular;
        letter-spacing: -0.5px;
        font-size: 2.5rem;
        margin-top: 2.5rem;
        margin-left: 1rem;
        color: white; }
    .top-categories-section .categories-wrapper .category1 {
      background: linear-gradient(to top, #d71a8d 0%, #f84327 100%); }
    .top-categories-section .categories-wrapper .category2 {
      background: linear-gradient(to top, #684dbe 0%, #2387dc 100%); }
    .top-categories-section .categories-wrapper .category3 {
      background: linear-gradient(to top, #523498 0%, #903071 100%); }
    .top-categories-section .categories-wrapper .category4 {
      background-image: linear-gradient(to top, #f794a4 0%, #fdd6bd 100%); }

.books-feed-section {
  margin-top: 5rem; }
  .books-feed-section .books-wrapper {
    display: flex;
    padding: 4rem 4rem 7rem 4rem;
    background: white; }
    .books-feed-section .books-wrapper .book {
      flex: 1;
      display: flex;
      margin: 0 2rem;
      padding: 2rem;
      border-radius: 6px;
      box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0.2), 0px 0px 0px 0px rgba(0, 0, 0, 0.14), 0px 0px 0px 0px rgba(0, 0, 0, 0.12);
      border-width: 1px;
      border-style: solid;
      border-color: #e0e0e0;
      margin-bottom: 1.5rem; }
      .books-feed-section .books-wrapper .book:hover {
        box-shadow: 0 1px 2px 0 rgba(60, 64, 67, 0.302), 0 1px 3px 1px rgba(60, 64, 67, 0.149); }
      .books-feed-section .books-wrapper .book:first-child {
        margin-left: 0; }
      .books-feed-section .books-wrapper .book:last-child {
        margin-right: 0; }
      .books-feed-section .books-wrapper .book img {
        width: 9.6rem;
        height: 13.5rem;
        border-radius: 0.5rem; }
      .books-feed-section .books-wrapper .book .content {
        margin-left: 1.5rem;
        position: relative; }
        .books-feed-section .books-wrapper .book .content h5 {
          font-family: Karla-Bold;
          letter-spacing: -0.5px;
          text-transform: capitalize;
          font-size: 2rem;
          margin-top: 5px;
          margin-bottom: 5px; }
        .books-feed-section .books-wrapper .book .content h6 {
          font-family: Karla-Regular;
          letter-spacing: -0.5px;
          font-size: 1.5rem;
          margin-top: 0px;
          opacity: 0.8; }
        .books-feed-section .books-wrapper .book .content a {
          font-family: Karla-Bold;
          letter-spacing: -0.5px;
          position: absolute;
          bottom: 0;
          font-size: 2rem;
          padding: 0.5rem;
          color: #6200ee;
          text-transform: capitalize;
          text-decoration: none;
          margin: 0; }
          .books-feed-section .books-wrapper .book .content a:hover {
            padding: 0.5rem;
            background-color: #ded7fc;
            border-radius: 4px;
            text-decoration: none; }

.line {
  position: relative;
  top: 50%;
  width: 22.5em;
  height: 5rem;
  margin: 0 auto;
  border-right: 2px solid transparent;
  font-size: 180%;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  transform: translateY(-50%); }

/*Animation*/
.anim-typewriter {
  animation: typewriter 4s steps(50) 1s 1 normal both; }

@keyframes typewriter {
  from {
    width: 0; }
  to {
    width: 22.5em; } }

/*# sourceMappingURL=styles.cs.map */
