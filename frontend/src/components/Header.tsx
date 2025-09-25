import { RxHamburgerMenu } from "react-icons/rx";
import { IoIosSearch } from "react-icons/io";
import Image from "next/image";
import logo from "@/assets/reddit-logo-small.png";

export default function Header() {
  return (
    <header className="px-4 py-2 flex items-center gap-4 border-b border-gray-300">
      <div className="flex-[0.3] flex items-center gap-4">
        <RxHamburgerMenu className="text-2xl" />
        <Image src={logo} alt="Reddit Logo" height={33} />
      </div>
      <div className="flex-[0.4] rounded-full border-gray-300 border px-2 py-2 text-sm flex items-center gap-2">
        <IoIosSearch className="inline text-2xl" />
        <input
          type="text"
          placeholder="Search Reddit"
          className="h-full w-full text-lg outline-none bg-transparent"
        />
      </div>
      <div className="flex-[0.3]">
        <button className="py-3 px-3 border border-gray-300 bg-accent-orange text-white rounded-full text-sm font-semibold hover:bg-accent-orange hover:brightness-90 transition-colors duration-300 ease-in-out">
          Log In
        </button>
      </div>
    </header>
  );
}
