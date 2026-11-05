"use client";

import React from "react";
import Link from "next/link";
import { Users, Mail, Heart } from "lucide-react";
import { useLanguage } from "@/lib/LanguageContext";

// Clean inline SVGs for Brand Icons
function LinkedInIcon({ className = "w-4 h-4" }: { className?: string }) {
  return (
    <svg
      className={className}
      fill="currentColor"
      viewBox="0 0 24 24"
      aria-hidden="true"
    >
      <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
    </svg>
  );
}

function GitHubIcon({ className = "w-4 h-4" }: { className?: string }) {
  return (
    <svg
      className={className}
      fill="currentColor"
      viewBox="0 0 24 24"
      aria-hidden="true"
    >
      <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
      />
    </svg>
  );
}

function InstagramIcon({ className = "w-4 h-4" }: { className?: string }) {
  return (
    <svg
      className={className}
      fill="currentColor"
      viewBox="0 0 24 24"
      aria-hidden="true"
    >
      <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
    </svg>
  );
}

export default function Footer() {
  const { t } = useLanguage();

  const socialLinks = [
    {
      name: "LinkedIn",
      href: "https://www.linkedin.com/in/shivani2302/",
      icon: LinkedInIcon,
      hoverClass: "hover:bg-[#0A66C2] hover:text-white",
      label: "LinkedIn Profile",
    },
    {
      name: "GitHub",
      href: "https://github.com/Shivaniroy09",
      icon: GitHubIcon,
      hoverClass: "hover:bg-[#24292e] hover:text-white",
      label: "GitHub Profile",
    },
    {
      name: "Instagram",
      href: "https://www.instagram.com/shivaniii.jpeg/",
      icon: InstagramIcon,
      hoverClass: "hover:bg-gradient-to-tr hover:from-[#f09433] hover:via-[#dc2743] hover:to-[#bc1888] hover:text-white",
      label: "Instagram Profile",
    },
    {
      name: "Email",
      href: "mailto:shivaniroy2309@gmail.com",
      icon: Mail,
      hoverClass: "hover:bg-primary hover:text-white",
      label: "Send Email",
    },
  ];

  return (
    <footer className="bg-navy text-white border-t border-navy-light" role="contentinfo">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-14">
        {/* Main 4-Column Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-10">
          {/* Column 1: Brand & Identity */}
          <div className="space-y-4">
            <Link href="/" className="flex items-center gap-2.5">
              <div className="w-9 h-9 bg-primary rounded-lg flex items-center justify-center">
                <Users className="w-5 h-5 text-white" />
              </div>
              <div>
                <span className="text-lg font-bold tracking-tight">{t("site.name")}</span>
              </div>
            </Link>
            <p className="text-blue-200 text-sm leading-relaxed">
              {t("site.footerDescription")}
            </p>
            <p className="text-xs text-blue-300/90 leading-relaxed italic">
              &ldquo;{t("site.tagline")}&rdquo;
            </p>

            <div className="pt-2">
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/10 text-xs text-blue-200 font-medium">
                <span>Verified Official Portals Only</span>
              </div>
            </div>
          </div>

          {/* Column 2: Discover Schemes */}
          <div>
            <h3 className="text-xs font-bold text-white mb-4 uppercase tracking-wider text-blue-200">
              {t("nav.findSchemes")}
            </h3>
            <ul className="space-y-2.5 text-sm">
              <li>
                <Link
                  href="/find-schemes"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  {t("nav.findSchemes")} (Wizard)
                </Link>
              </li>
              <li>
                <Link
                  href="/categories"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  {t("nav.categories")}
                </Link>
              </li>
              <li>
                <Link
                  href="/central-schemes"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  {t("nav.centralSchemes")}
                </Link>
              </li>
              <li>
                <Link
                  href="/state-schemes"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  {t("nav.stateSchemes")} (36 States/UTs)
                </Link>
              </li>
              <li>
                <Link
                  href="/compare"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  Compare Schemes
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 3: Platform & Transparency */}
          <div>
            <h3 className="text-xs font-bold text-white mb-4 uppercase tracking-wider text-blue-200">
              {t("nav.about")}
            </h3>
            <ul className="space-y-2.5 text-sm">
              <li>
                <Link
                  href="/how-it-works"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  {t("nav.howItWorks")}
                </Link>
              </li>
              <li>
                <Link
                  href="/about"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  {t("nav.about")} SchemeSaathi
                </Link>
              </li>
              <li>
                <Link
                  href="/privacy"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  {t("nav.privacy")} Policy (Zero Documents)
                </Link>
              </li>
              <li>
                <Link
                  href="/disclaimer"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  {t("nav.disclaimer")}
                </Link>
              </li>
              <li>
                <Link
                  href="/contact"
                  className="text-blue-200 hover:text-white transition-colors"
                >
                  {t("nav.reportIssue")}
                </Link>
              </li>
              <li className="pt-1 border-t border-navy-light/60">
                <a
                  href="/presentation.html"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1.5 text-xs text-sky-300 hover:text-white font-medium transition-colors"
                >
                  <span>📊 Project Presentation Deck</span>
                </a>
              </li>
              <li>
                <a
                  href="/SchemeSaathi_Presentation.pptx"
                  download
                  className="inline-flex items-center gap-1.5 text-xs text-sky-400 hover:text-white transition-colors"
                >
                  <span>📥 Download Slide Deck (.pptx)</span>
                </a>
              </li>
            </ul>
          </div>

          {/* Column 4: Developer Credit & Social Connect */}
          <div className="space-y-4">
            <h3 className="text-xs font-bold text-white mb-4 uppercase tracking-wider text-blue-200">
              Developer & Connect
            </h3>
            <p className="text-xs text-blue-200 leading-relaxed">
              Designed & Developed by <strong className="text-white">Shivani</strong> as an independent civic-tech platform for public empowerment.
            </p>

            {/* Social Icons Strip */}
            <div className="flex flex-wrap items-center gap-2 pt-1">
              {socialLinks.map((item) => {
                const Icon = item.icon;
                return (
                  <a
                    key={item.name}
                    href={item.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className={`w-9 h-9 rounded-lg bg-white/10 text-blue-100 flex items-center justify-center transition-all ${item.hoverClass}`}
                    aria-label={item.label}
                    title={`${item.name} - Shivani`}
                  >
                    <Icon className="w-4 h-4" />
                  </a>
                );
              })}
            </div>

            {/* Contact Email Link */}
            <div className="pt-2">
              <a
                href="mailto:shivaniroy2309@gmail.com"
                className="inline-flex items-center gap-1.5 text-xs text-blue-200 hover:text-white transition-colors group break-all"
              >
                <Mail className="w-3.5 h-3.5 text-primary-light shrink-0" />
                <span className="group-hover:underline">shivaniroy2309@gmail.com</span>
              </a>
            </div>
          </div>
        </div>

        {/* Global Copyright & Creator Credit Bar */}
        <div className="mt-12 pt-8 border-t border-white/15">
          <div className="flex flex-col md:flex-row items-center justify-between gap-4 text-center md:text-left">
            <div className="space-y-1">
              <p className="text-xs text-blue-300">
                © {new Date().getFullYear()} <strong className="text-white">SchemeSaathi</strong>. All rights reserved.
              </p>
              <p className="text-[11px] text-blue-400 max-w-xl">
                {t("site.footerDisclaimer")}
              </p>
            </div>

            {/* Prominent Developed & Designed by Shivani Badge */}
            <div className="flex flex-col sm:flex-row items-center gap-2 text-xs text-blue-200 bg-white/5 border border-white/10 px-4 py-2.5 rounded-xl">
              <span className="flex items-center gap-1.5">
                <span>Designed &amp; Developed with</span>
                <Heart className="w-3.5 h-3.5 text-red-400 fill-red-400 inline" />
                <span>by</span>
                <strong className="text-white font-semibold">Shivani</strong>
              </span>
              <span className="hidden sm:inline text-white/30">•</span>
              <div className="flex items-center gap-2">
                <a
                  href="https://www.linkedin.com/in/shivani2302/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-300 hover:text-white font-medium underline underline-offset-2 transition-colors"
                >
                  LinkedIn
                </a>
                <span className="text-white/30">•</span>
                <a
                  href="https://github.com/Shivaniroy09"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-300 hover:text-white font-medium underline underline-offset-2 transition-colors"
                >
                  GitHub
                </a>
                <span className="text-white/30">•</span>
                <a
                  href="https://www.instagram.com/shivaniii.jpeg/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-300 hover:text-white font-medium underline underline-offset-2 transition-colors"
                >
                  Instagram
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
