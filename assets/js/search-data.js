// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "About",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-projects",
          title: "Projects",
          description: "A growing collection of your cool projects.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-repositories",
          title: "Repositories",
          description: "A list of my public repositories.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "Curriculum Vitae of Enea Manzi - Cyber Security Student &amp; Software Developer",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-bookshelf",
          title: "bookshelf",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/books/";
          },
        },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/en/the_godfather.html";
            },},{id: "projects-exhibition-webapp",
          title: 'Exhibition Webapp',
          description: "TODO A dynamic web application serving as a digital portfolio.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/en/exhibition-webapp.html";
            },},{id: "projects-ftp-client-amp-server",
          title: 'FTP Client &amp;amp; Server',
          description: "TODO Developed a multi-threaded FTP-compliant client-server application in C for file transfer, fully interoperable with FileZilla.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/en/ftp-server.html";
            },},{id: "projects-template-back-ground-image",
          title: 'Template Back Ground Image',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/en/template-bg-image.html";
            },},{id: "projects-template-redirect-site",
          title: 'Template Redirect Site',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/en/template-redirect-site.html";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%65%6E%65%61.%6D%61%6E%7A%69@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/eneamanzi", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/eneamanzi", "_blank");
        },
      },{
        id: 'social-cv',
        title: 'CV',
        section: 'Socials',
        handler: () => {
          window.open("/assets/pdf/cv_italian.pdf", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
