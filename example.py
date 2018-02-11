from flaxcli import FlaxCli

if __name__ == '__main__':
    sample_text = """
        Uhm, yeah I’d bet that maybe fifty percent, and possibly even more of Americans, uh, don’t speak, 
        uh, any language other than English. Uhm, from grade school through high school, uh, people are 
        generally given the option to study a popular foreign language like Spanish or French. Uhm, and 
        some schools are even offering, you know, classes in, uh, Chinese, Japanese and Arabic. So, it really 
        depends on the school; uhm, however, unlike a lot of, you know, maybe countries in Europe, uhm, 
        the vast majority of kids in America don’t actually learn how to speak, uhm, or just communicate 
        effectively in the foreign languages that they’re taught in school. Uhm, there are exceptions of 
        course, uhm and in some schools, you know, all classes are taught in a foreign language, like French, 
        so it goes without saying kids are – are learning how to speak that language. Uhm, but currently, 
        most Americans probably are uh, monolingual, and uhm, even wh–, you know, when they travel abroad, 
        uh, they’re able to use, uh, English basically wherever they go, so that’s another real, uh, 
        disincentive to actually, uhm, become fluent in a foreign language.
    """

    client = FlaxCli()
    collocations = client.query_text(sample_text)

    print(collocations)
