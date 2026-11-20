import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Қадам (Проект-тест)",
  description: "Оқу процесін, тестілеуді және жергілікті LLM мүмкіндіктерін біріктіретін платформа",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="kk">
      <body style={{ margin: 0 }}>{children}</body>
    </html>
  );
}
